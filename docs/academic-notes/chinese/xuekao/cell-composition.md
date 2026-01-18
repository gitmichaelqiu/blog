---
hide:
  - toc
comments: true
---

<style>
  /* Ensure the container is adaptive and fills the page */
  #map-wrapper {
    width: 100%;
    height: 85vh; 
    border: 1px solid var(--md-typeset-table-color);
    background-color: var(--md-main-bg-color);
    overflow: hidden;
    position: relative;
  }

  /* Target the SVG specifically for Dark Mode */
  [data-md-color-scheme="slate"] #cell-svg {
    filter: invert(0.9) hue-rotate(180deg);
    background-color: #1e1e1e; /* Match your site's dark background */
  }

  #cell-svg {
    width: 100%;
    height: 100%;
    display: block;
  }
</style>

<div id="map-wrapper">
    <embed id="cell-svg" type="image/svg+xml" src="../cell-composition.svg" />
</div>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
<script>
  window.onload = function() {
    const svgElement = document.getElementById('cell-svg');
    const wrapper = document.getElementById('map-wrapper');

    const panZoom = svgPanZoom('#cell-svg', {
      zoomEnabled: true,
      controlIconsEnabled: true,
      fit: true,
      center: true,
      mouseWheelZoomEnabled: true
    });

    // BLOCK PAGE SCROLL: Force-prevent scroll when mouse is inside the wrapper
    window.addEventListener('wheel', function(e) {
      const rect = wrapper.getBoundingClientRect();
      const isInside = (
        e.clientX >= rect.left &&
        e.clientX <= rect.right &&
        e.clientY >= rect.top &&
        e.clientY <= rect.bottom
      );

      if (isInside) {
        e.preventDefault();
      }
    }, { passive: false });

    window.addEventListener('resize', function() {
      panZoom.resize();
    });
  };
</script>