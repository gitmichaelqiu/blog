---
comments: true
---

## Where to customize prompts?

In `LexiGenAssets/settings.yaml`.

If you want to write a prompt with multiple lines, follow this format:

```text
key: |
  line 1
  line 2
  line 3
```

## Sentence Generation Prompt

**Default Prompt**:

```text
Create a simple sentence using the word '{word}'. The sentence should be clear and educational.
```

**Placeholders**:

- `{word}`

## Analysis Prompt

**Default Prompt**:

```text
Analyze the grammatical usage of '{word}' in this sentence: '{sentence}'
Focus on:
1. Tense (e.g., Present Simple, Past Perfect)
2. Voice (Active/Passive)
3. Mood (Indicative/Subjunctive)
4. Function (e.g., Subject, Object, Modifier)

Keep the analysis concise and technical. Output in 1 line. Example format:
"Present Simple, Active Voice. Functions as the subject of the sentence."
```

**Placeholders**:

- `{word}`
- `{sentence}`

## Designation Prompt

**Default Prompt**:

```text
Create a simple sentence using the word '{word}' using {tense} tense. The sentence should be clear and educational.
```

**Placeholders**:

- `{word}`
- `{tense}`

## Contributing

If you have any better prompts, post here [GitHub Discussion #20](https://github.com/gitmichaelqiu/LexiGen/discussions/20).

Thank you for your contribution 🫶.
