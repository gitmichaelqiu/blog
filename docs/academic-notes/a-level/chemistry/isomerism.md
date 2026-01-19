---
hide:
  - toc
comments: true
---

# Isomerism

<style>
  #map-wrapper {
    width: 100%;
    height: 90vh;
    border: 1px solid var(--md-typeset-table-color);
    background-color: var(--md-main-bg-color);
    overflow: hidden;
  }

  [data-md-color-scheme="slate"] #cell-svg {
    filter: invert(0.9) hue-rotate(180deg);
  }
</style>

<div id="map-wrapper">
    <embed id="cell-svg" type="image/svg+xml" src="../isomerism.svg" style="width:100%; height:100%;"/>
</div>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
<script>
  const svgEmbed = document.getElementById('cell-svg');

  svgEmbed.addEventListener('load', function() {
    const panZoom = svgPanZoom('#cell-svg', {
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
  });
</script>