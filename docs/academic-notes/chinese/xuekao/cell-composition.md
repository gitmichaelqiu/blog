<div id="map-wrapper" style="width: 100%; height: 80vh; border: 1px solid var(--md-typeset-table-color); overflow: hidden; background-color: var(--md-main-bg-color); touch-action: none;">
    <embed id="cell-svg" type="image/svg+xml" src="../cell-composition.svg" style="width: 100%; height: 100%; pointer-events: all;"/>
</div>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
<script>
  window.onload = function() {
    const container = document.getElementById('map-wrapper');
    
    const panZoom = svgPanZoom('#cell-svg', {
      zoomEnabled: true,
      controlIconsEnabled: true,
      fit: true,
      center: true,
      mouseWheelZoomEnabled: true, // Ensures the wheel zooms the SVG
      preventMouseEventsDefault: true // Stops the browser from scrolling the page
    });

    // Explicitly prevent scroll propagation to the window
    container.addEventListener('wheel', function(e) {
      e.preventDefault();
    }, { passive: false });

    window.addEventListener('resize', function() {
      panZoom.resize();
      panZoom.fit();
      panZoom.center();
    });
  };
</script>