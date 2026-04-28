const initPanZoomLoader = () => {
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

        // Skip if already initialized
        if (wrapper.querySelector('embed')) return;

        let panZoomInstance = null;
        let svgElement = null;

        const initPanZoom = () => {
            if (panZoomInstance) return;

            svgElement = document.createElement('embed');
            svgElement.id = 'cell-svg';
            svgElement.type = 'image/svg+xml';
            svgElement.src = svgSrc;
            svgElement.style.width = '100%';
            svgElement.style.height = '100%';
            
            wrapper.appendChild(svgElement);

            loadScript(() => {
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
};

// Initial load
document.addEventListener("DOMContentLoaded", initPanZoomLoader);

// Handle SPA transitions (MkDocs Material / Zensical)
// Use multiple common events to be safe
window.addEventListener("locationChange", initPanZoomLoader);
window.addEventListener("popstate", initPanZoomLoader);
// Some versions use this specific event for content updates
document.addEventListener("DOMNodeInserted", (e) => {
    if (e.target.id === "map-wrapper" || (e.target.querySelector && e.target.querySelector("#map-wrapper"))) {
        initPanZoomLoader();
    }
}, false);
