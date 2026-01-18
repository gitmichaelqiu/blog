---
hide:
  - toc
comments: true
---

# 细胞的分子组成

<style>
  #map-wrapper {
    width: 100%;
    height: 90vh; /* Fills most of the viewport height */
    border: 1px solid var(--md-typeset-table-color);
    background-color: var(--md-main-bg-color);
    overflow: hidden;
  }

  /* Adaptive Dark Mode Filter */
  [data-md-color-scheme="slate"] #cell-svg {
    filter: invert(0.9) hue-rotate(180deg);
  }
</style>

<div id="map-wrapper">
    <embed id="cell-svg" type="image/svg+xml" src="../cell-composition.svg" style="width:100%; height:100%;"/>
</div>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
<script>
  const svgEmbed = document.getElementById('cell-svg');

  svgEmbed.addEventListener('load', function() {
    // 1. Initialize Pan-Zoom
    const panZoom = svgPanZoom('#cell-svg', {
      zoomEnabled: true,
      controlIconsEnabled: true,
      fit: true,
      center: true,
      mouseWheelZoomEnabled: true
    });

    // 2. Reach inside the SVG document to kill the scroll event
    const svgDoc = svgEmbed.getSVGDocument();
    
    if (svgDoc) {
      // This stops the wheel event inside the embed from bubbling up to the main page
      svgDoc.addEventListener('wheel', function(e) {
        e.preventDefault();
      }, { passive: false });
    }

    // 3. Keep it responsive
    window.addEventListener('resize', function() {
      panZoom.resize();
    });
  });
</script>