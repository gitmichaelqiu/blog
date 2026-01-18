<div id="svg-container" style="width: 100%; height: 500px; border: 1px solid #ccc;">
    <embed id="cell-svg" type="image/svg+xml" src="../cell-composition.svg" style="width: 100%; height: 100%;"/>
</div>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
<script>
  window.onload = function() {
    svgPanZoom('#cell-svg', {
      zoomEnabled: true,
      controlIconsEnabled: true,
      fit: true,
      center: true,
    });
  };
</script>