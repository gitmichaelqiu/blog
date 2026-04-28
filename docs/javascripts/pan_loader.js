/**
 * Lightweight loader for svg-pan-zoom to prevent heavy memory usage on page load.
 * Only initializes the panning library when the user interacts with the SVG.
 */
document.addEventListener("DOMContentLoaded", function() {
    // Find all SVG containers that were previously using svg-pan-zoom
    const mapWrappers = document.querySelectorAll('#map-wrapper');
    
    mapWrappers.forEach(wrapper => {
        const svgEmbed = wrapper.querySelector('embed[type="image/svg+xml"], object[type="image/svg+xml"]');
        if (!svgEmbed) return;

        // Function to initialize pan-zoom
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

                    // Fix for wheel event in some browsers
                    const svgDoc = svgEmbed.getSVGDocument();
                    if (svgDoc) {
                        svgDoc.addEventListener('wheel', function(e) {
                            e.preventDefault();
                        }, { passive: false });
                    }

                    window.addEventListener('resize', function() {
                        panZoom.resize();
                    });
                    
                    console.log("SVG Pan-Zoom initialized on demand.");
                } catch (e) {
                    console.error("Failed to initialize SVG Pan-Zoom:", e);
                }
            } else {
                // Load script if not available
                const script = document.createElement('script');
                script.src = "https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js";
                script.onload = initPanZoom;
                document.head.appendChild(script);
            }
        };

        // Activate on click or touch
        const activate = (e) => {
            wrapper.removeEventListener('click', activate);
            wrapper.removeEventListener('touchstart', activate);
            initPanZoom();
            // Remove the "inactive" state from wrapper if any
            wrapper.classList.remove('pan-zoom-inactive');
        };

        wrapper.classList.add('pan-zoom-inactive');
        wrapper.addEventListener('click', activate);
        wrapper.addEventListener('touchstart', activate);
        
        // Add a small visual hint that it's interactive
        const hint = document.createElement('div');
        hint.className = 'pan-zoom-hint';
        hint.innerHTML = '<span>Click to Enable Zoom & Pan</span>';
        wrapper.appendChild(hint);
    });
});
