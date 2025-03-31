[Standalone Webpage with the Copy Function](https://gitmichaelqiu.github.io/Discord-Spoiler-Generator/)

<div class="text-transformer-container">
<style>
.text-transformer-container {
    /* Reset container styling for MkDocs integration */
    box-sizing: border-box;
    max-width: 800px;
    margin: 0 auto;
    padding: 1rem;
    font-family: var(--md-text-font-family);
}

.text-transformer-container * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

.text-transformer {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background: var(--md-default-bg-color);
    padding: 1.5rem;
    border-radius: 0.25rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.text-transformer h2 {
    color: var(--md-primary-fg-color);
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.text-transformer textarea {
    width: 100%;
    min-height: 100px;
    padding: 0.8rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.25rem;
    background: var(--md-code-bg-color);
    color: var(--md-code-fg-color);
    font-family: var(--md-code-font-family);
    resize: vertical;
}

.text-transformer .mode-selector {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.text-transformer .radio-group {
    display: flex;
    gap: 0.5rem;
}

.text-transformer .radio-label {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    cursor: pointer;
}
</style>

<div class="text-transformer">
    <div class="mode-selector">
        <div class="radio-group">
            <label class="radio-label">
                <input type="radio" name="mode" value="word" checked>
                Word Mode
            </label>
            <label class="radio-label">
                <input type="radio" name="mode" value="original">
                Character Mode
            </label>
        </div>
    </div>

    <textarea id="input" placeholder="Enter text to transform..."></textarea>
    <textarea id="output" readonly placeholder="Transformed text will appear here..."></textarea>
</div>

<script>
(function() {
    // Scoped JavaScript to prevent conflicts
    function sandwichCharacters(str) {
        const parts = str.split(':');
        const wrappedParts = parts.map((part, index) => {
            if (index % 2 === 0) {
                return Array.from(part).map(c => `||${c}||`).join('');
            } else {
                return part.includes(' ') 
                    ? Array.from(str).map(c => `||${c}||`).join('')
                    : `||:${part}:||`;
            }
        });
        return wrappedParts.join('');
    }

    function wordModeTransform(str) {
        return str.split(/\s+/)
                  .filter(word => word.length > 0)
                  .map(word => `||${word}||`)
                  .join(' ');
    }

    function updateOutput() {
        const inputText = document.getElementById('input').value;
        const mode = document.querySelector('.text-transformer-container input[name="mode"]:checked').value;
        const outputText = mode === 'word' ? wordModeTransform(inputText) : sandwichCharacters(inputText);
        document.getElementById('output').value = outputText;
    }

    // Event listeners
    document.querySelector('.text-transformer-container #input').addEventListener('input', updateOutput);
    document.querySelectorAll('.text-transformer-container input[name="mode"]').forEach(radio => {
        radio.addEventListener('change', updateOutput);
    });
})();
</script>
</div>