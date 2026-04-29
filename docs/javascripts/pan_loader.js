/**
 * pan_loader.js
 * Handles lazy-loading and initializing pan-zoom for SVG mindmaps.
 * Supports SPA transitions and subpath deployments (like GitHub Pages /blog/).
 */

function initSVGPanZoom() {
    const mapWrappers = document.querySelectorAll('#map-wrapper');
    if (mapWrappers.length === 0) return;

    mapWrappers.forEach(wrapper => {
        const linkEl = wrapper.querySelector('link');
        let svgSrc = linkEl ? linkEl.getAttribute('href') : null;
        if (!svgSrc) return;

        // Skip if already initialized
        if (wrapper.querySelector('embed')) return;

        // --- SUBPATH HANDLING (GitHub Pages /blog/) ---
        // If the path is root-relative (starts with /) but missing the /blog prefix
        if (svgSrc.startsWith('/') && !svgSrc.startsWith('/blog/')) {
            // Check if current page is under /blog/ (deployed site)
            if (window.location.pathname.startsWith('/blog/')) {
                svgSrc = '/blog' + svgSrc;
            }
        }

        const embed = document.createElement('embed');
        embed.setAttribute('id', 'cell-svg');
        embed.setAttribute('type', 'image/svg+xml');
        embed.setAttribute('src', svgSrc);
        embed.style.width = '100%';
        embed.style.height = '100%';

        embed.addEventListener('load', () => {
            const svgDoc = embed.getSVGDocument();
            if (svgDoc) {
                // Initialize svg-pan-zoom
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

// Support for Instant Navigation (SPA transitions)
if (window.location.href.includes('instant')) {
    // Some themes use different events for SPA transitions
    document.addEventListener('DOMNodeInserted', (e) => {
        if (e.target.id === 'map-wrapper') initSVGPanZoom();
    });
}

// Observe for dynamic content changes (more robust for SPAs)
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
            initSVGPanZoom();
        }
    });
});

observer.observe(document.body, { childList: true, subtree: true });
