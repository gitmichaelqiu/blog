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
            while (pendingInits.length) { pendingInits.shift()(); }
        };
        script.onerror = () => {
            isScriptLoading = false;
            console.error("Failed to load svg-pan-zoom script.");
        };
        document.head.appendChild(script);
    };

    mapWrappers.forEach(wrapper => {
        const svgSrc = wrapper.getAttribute('data-src');
        if (!svgSrc) return;

        let panZoomInstance = null;
        let svgElement = null;

        const initPanZoom = () => {
            if (panZoomInstance) return;

            // Create the embed element dynamically
            svgElement = document.createElement('embed');
            svgElement.id = 'cell-svg';
            svgElement.type = 'image/svg+xml';
            svgElement.src = svgSrc;
            svgElement.style.width = '100%';
            svgElement.style.height = '100%';
            
            wrapper.appendChild(svgElement);

            loadScript(() => {
                // Wait for the SVG to load before initializing pan-zoom
                svgElement.addEventListener('load', function() {
                    try {
                        if (panZoomInstance) return;

                        panZoomInstance = window.svgPanZoom(svgElement, {
                            zoomEnabled: true,
                            controlIconsEnabled: true,
                            fit: true,
                            center: true,
                            mouseWheelZoomEnabled: true
                        });

                        const svgDoc = svgElement.getSVGDocument();
                        if (svgDoc) {
                            svgDoc.addEventListener('wheel', function(e) {
                                e.preventDefault();
                            }, { passive: false });
                        }

                        const handleResize = () => {
                            if (panZoomInstance) panZoomInstance.resize();
                        };
                        window.addEventListener('resize', handleResize);

                        // Cleanup logic
                        const cleanup = () => {
                            if (panZoomInstance) {
                                panZoomInstance.destroy();
                                panZoomInstance = null;
                            }
                            window.removeEventListener('resize', handleResize);
                            if (svgElement && svgElement.parentNode) {
                                svgElement.parentNode.removeChild(svgElement);
                            }
                        };

                        // Use MutationObserver or custom event for cleanup if needed
                        // For non-SPA, this runs once per page. 
                        // For SPA, we might need a global cleanup on navigation.

                    } catch (e) {
                        console.error("Failed to initialize SVG Pan-Zoom:", e);
                    }
                });
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
