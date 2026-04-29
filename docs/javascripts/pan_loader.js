/**
 * pan_loader.js
 * Handles lazy-loading and initializing pan-zoom for SVG mindmaps.
 */

(function() {
    function initializeWrapper(wrapper) {
        const linkEl = wrapper.querySelector('link');
        const svgSrc = linkEl ? linkEl.getAttribute('href') : null;
        if (!svgSrc) return;

        // Skip if already has an embed
        if (wrapper.querySelector('embed')) return;

        const embed = document.createElement('embed');
        embed.setAttribute('class', 'pan-zoom-svg');
        embed.setAttribute('type', 'image/svg+xml');
        embed.setAttribute('src', svgSrc);
        embed.style.width = '100%';
        embed.style.height = '100%';

        const tryInit = () => {
            if (!window.svgPanZoom) {
                console.warn('svgPanZoom not loaded yet, retrying...');
                setTimeout(tryInit, 100);
                return;
            }

            try {
                window.svgPanZoom(embed, {
                    zoomEnabled: true,
                    controlIconsEnabled: true,
                    fit: true,
                    center: true,
                    minZoom: 0.1,
                    maxZoom: 10
                });
            } catch (e) {
                console.error('Failed to initialize svgPanZoom:', e);
            }
        };

        embed.addEventListener('load', tryInit);
        
        // Prevent page scroll when mouse is over the SVG and scrolling (zooming)
        wrapper.addEventListener('wheel', (e) => {
            if (e.ctrlKey || e.metaKey || true) { // Always prevent if we want zoom to be exclusive
                e.preventDefault();
            }
        }, { passive: false });

        wrapper.appendChild(embed);
    }

    function scanAndInit() {
        // Look for any div with id="map-wrapper"
        const mapWrappers = document.querySelectorAll('#map-wrapper');
        mapWrappers.forEach(initializeWrapper);
    }

    // Initial check
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', scanAndInit);
    } else {
        scanAndInit();
    }

    // Observe for dynamic content changes (SPA transitions)
    const observer = new MutationObserver((mutations) => {
        let shouldScan = false;
        for (const mutation of mutations) {
            if (mutation.addedNodes.length) {
                shouldScan = true;
                break;
            }
        }
        if (shouldScan) scanAndInit();
    });

    observer.observe(document.documentElement, { childList: true, subtree: true });
})();
