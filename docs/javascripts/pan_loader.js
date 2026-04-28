/**
 * Lightweight loader for svg-pan-zoom to prevent heavy memory usage on page load.
 * Only initializes the panning library when the user interacts with the SVG.
 */
document.addEventListener("DOMContentLoaded", function() {
    const mapWrappers = document.querySelectorAll('#map-wrapper');
    
    mapWrappers.forEach(wrapper => {
        const svgEmbed = wrapper.querySelector('embed[type="image/svg+xml"], object[type="image/svg+xml"]');
        if (!svgEmbed) return;

        const initPanZoom = () => {
            if (window.svgPanZoom) {
                try {
                    const panZoom = window.svgPanZoom(svgEmbed, {
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

                    window.addEventListener('resize', function() {
                        panZoom.resize();
                    });
                } catch (e) {
                    console.error("Failed to initialize SVG Pan-Zoom:", e);
                }
            } else {
                const script = document.createElement('script');
                script.src = "https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js";
                script.onload = initPanZoom;
                document.head.appendChild(script);
            }
        };

        // Use Intersection Observer to initialize when visible
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    initPanZoom();
                    observer.unobserve(wrapper);
                }
            });
        }, { threshold: 0.1 });

        observer.observe(wrapper);
    });
});
