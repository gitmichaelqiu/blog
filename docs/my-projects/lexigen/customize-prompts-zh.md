---
comments: true
---

## 在哪里自定义提示词？

在 `LexiGenAssets/settings.yaml`.

如果你想写多行的提示词，请使用以下格式：

```text
选项: |
  行 1
  行 2
  行 3
```

## 生成句子提示词

**提示词标签**:

```text
generation_prompt
```

**默认提示词**:

```text
Create a simple sentence using the word '{word}'. The sentence should be clear and educational.
```

**占位符**:

- `{word}`

## 分析句子提示词

**提示词标签**:

```text
analysis_prompt
```

**默认提示词**:

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

**占位符**:

- `{word}`
- `{sentence}`

## 指定语法提示词


**提示词标签**:

```text
tense_prompt
```

**默认提示词**:

```text
Create a simple sentence using the word '{word}' using {tense} tense. The sentence should be clear and educational.
```

**占位符**:

- `{word}`
- `{tense}`

## 贡献

如果你有更好的提示词, 请在这里讨论 [GitHub Discussion #20](https://github.com/gitmichaelqiu/LexiGen/discussions/20).

感谢你的支持 🫶.
