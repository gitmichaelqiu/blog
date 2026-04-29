/**
 * pan_loader.js
 * Handles lazy-loading and initializing pan-zoom for SVG mindmaps.
 */

function initSVGPanZoom() {
    const mapWrappers = document.querySelectorAll('#map-wrapper');
    if (mapWrappers.length === 0) return;

    mapWrappers.forEach(wrapper => {
        const linkEl = wrapper.querySelector('link');
        const svgSrc = linkEl ? linkEl.getAttribute('href') : null;
        if (!svgSrc) return;

        // Skip if already initialized
        if (wrapper.querySelector('embed')) return;

        const embed = document.createElement('embed');
        embed.setAttribute('id', 'cell-svg');
        embed.setAttribute('type', 'image/svg+xml');
        embed.setAttribute('src', svgSrc);
        embed.style.width = '100%';
        embed.style.height = '100%';

        embed.addEventListener('load', () => {
            const svgDoc = embed.getSVGDocument();
            if (svgDoc) {
                if (window.svgPanZoom) {
                    window.svgPanZoom(embed, {
                        zoomEnabled: true,
                        controlIconsEnabled: true,
                        fit: true,
                        center: true,
                        minZoom: 0.1,
                        maxZoom: 10
                    });
                }
            }
        });

        wrapper.appendChild(embed);
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', initSVGPanZoom);

// Observe for dynamic content changes (SPA transitions)
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
            initSVGPanZoom();
        }
    });
});

observer.observe(document.body, { childList: true, subtree: true });
