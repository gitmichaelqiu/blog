/**
 * Lightweight loader for svg-pan-zoom to prevent heavy memory usage on page load.
 * Only initializes the panning library when the user interacts with the SVG.
 */
document.addEventListener("DOMContentLoaded", function() {
    const mapWrappers = document.querySelectorAll('#map-wrapper');
    if (mapWrappers.length === 0) return;

    let isScriptLoading = false;
    const pendingInits = [];

    const loadScript = (callback) => {
        if (window.svgPanZoom) {
            callback();
            return;
        }
        pendingInits.push(callback);
        if (isScriptLoading) return;
        isScriptLoading = true;

        const script = document.createElement('script');
        script.src = "https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js";
        script.onload = () => {
            isScriptLoading = false;
            while (pendingInits.length) pendingInits.shift()();
        };
        script.onerror = () => {
            isScriptLoading = false;
            console.error("Failed to load svg-pan-zoom script.");
        };
        document.head.appendChild(script);
    };

    // Shared Intersection Observer for efficiency
    const intersectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const wrapper = entry.target;
                const initFn = wrapper._initPanZoom;
                if (initFn) initFn();
                intersectionObserver.unobserve(wrapper);
            }
        });
    }, { threshold: 0.1 });

    mapWrappers.forEach(wrapper => {
        const svgEmbed = wrapper.querySelector('embed[type="image/svg+xml"], object[type="image/svg+xml"]');
        if (!svgEmbed) return;

        let panZoomInstance = null;
        let resizeHandler = null;

        const cleanup = () => {
            if (panZoomInstance) {
                try {
                    panZoomInstance.destroy();
                } catch (e) {}
                panZoomInstance = null;
            }
            if (resizeHandler) {
                window.removeEventListener('resize', resizeHandler);
                resizeHandler = null;
            }
        };

        wrapper._initPanZoom = () => {
            if (panZoomInstance) return;
            
            loadScript(() => {
                try {
                    if (panZoomInstance || !document.body.contains(wrapper)) return;

                    panZoomInstance = window.svgPanZoom(svgEmbed, {
                        zoomEnabled: true,
                        controlIconsEnabled: true,
                        fit: true,
                        center: true,
                        mouseWheelZoomEnabled: true
                    });

                    resizeHandler = () => {
                        if (panZoomInstance) panZoomInstance.resize();
                    };
                    window.addEventListener('resize', resizeHandler);

                    // Add wheel fix directly to the embed if possible
                    svgEmbed.addEventListener('wheel', (e) => e.preventDefault(), { passive: false });

                } catch (e) {
                    console.error("Failed to initialize SVG Pan-Zoom:", e);
                }
            });
        };

        // Listen for page unload/navigation to cleanup
        window.addEventListener('beforeunload', cleanup);
        
        // Use MutationObserver for cases where elements are removed without page reload
        const mutationObserver = new MutationObserver(() => {
            if (!document.body.contains(wrapper)) {
                cleanup();
                mutationObserver.disconnect();
            }
        });
        if (wrapper.parentNode) {
            mutationObserver.observe(wrapper.parentNode, { childList: true });
        }

        intersectionObserver.observe(wrapper);
    });
});
