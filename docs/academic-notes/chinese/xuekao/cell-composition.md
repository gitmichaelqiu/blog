<div id="map-wrapper" style="width: 100%; height: 80vh; border: 1px solid var(--md-typeset-table-color); overflow: hidden; background-color: var(--md-main-bg-color);">
    <embed id="cell-svg" type="image/svg+xml" src="../cell-composition.svg" style="width: 100%; height: 100%;"/>
</div>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
<script>
  window.onload = function() {
    const panZoom = svgPanZoom('#cell-svg', {
      zoomEnabled: true,
      controlIconsEnabled: true,
      fit: true,
      center: true,
      minZoom: 0.1,
      maxZoom: 10
    });

    window.addEventListener('resize', function() {
      panZoom.resize();
      panZoom.fit();
      panZoom.center();
    });
  };
</script>