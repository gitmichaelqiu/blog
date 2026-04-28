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
            while (pendingInits.length) {
                pendingInits.shift()();
            }
        };
        script.onerror = () => {
            isScriptLoading = false;
            console.error("Failed to load svg-pan-zoom script.");
        };
        document.head.appendChild(script);
    };

    mapWrappers.forEach(wrapper => {
        const svgEmbed = wrapper.querySelector('embed[type="image/svg+xml"], object[type="image/svg+xml"]');
        if (!svgEmbed) return;

        let panZoomInstance = null;

        const initPanZoom = () => {
            if (panZoomInstance) return;
            
            loadScript(() => {
                try {
                    // Double check if already initialized (race condition)
                    if (panZoomInstance) return;

                    panZoomInstance = window.svgPanZoom(svgEmbed, {
                        zoomEnabled: true,
                        controlIconsEnabled: true,
                        fit: true,
                        center: true,
                        mouseWheelZoomEnabled: true
                    });

                    const svgDoc = svgEmbed.getSVGDocument();
                    if (svgDoc) {
                        svgDoc.addEventListener('wheel', function(e) {
                            e.preventDefault();
                        }, { passive: false });
                    }

                    const handleResize = () => {
                        if (panZoomInstance) panZoomInstance.resize();
                    };
                    window.addEventListener('resize', handleResize);
                    
                    // Optional: Cleanup if wrapper is removed (for SPAs)
                    const observer = new MutationObserver((mutations) => {
                        if (!document.body.contains(wrapper)) {
                            if (panZoomInstance) {
                                panZoomInstance.destroy();
                                panZoomInstance = null;
                            }
                            window.removeEventListener('resize', handleResize);
                            observer.disconnect();
                        }
                    });
                    observer.observe(wrapper.parentNode, { childList: true });

                } catch (e) {
                    console.error("Failed to initialize SVG Pan-Zoom:", e);
                }
            });
        };

        const intersectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    initPanZoom();
                    intersectionObserver.unobserve(wrapper);
                }
            });
        }, { threshold: 0.1 });

        intersectionObserver.observe(wrapper);
    });
});
