---
comments: true
date:
  created: 2024-09-14
  updated: 2024-09-15
categories:
  - AI
---

## Ollama

### What Is Ollama?

Ollama is an open-source platform designed to make large language models (LLMs) more accessible and usable.

### How to Deploy

1. Visit [Ollama](https://ollama.com/) and download.
2. Choose a model you like
3. Run `ollama run YourModel:ParameterSize` in the terminal or Windows CMD (Windows: Win+R $\rightarrow$ cmd)
4. Your model will start downloading. If the model has already been downloaded, you will go to the chat page (starts with `>>>`);

### How to Choose An Appropriate Model

#### Choose Model

Visit [Model Library](https://ollama.com/library)

Here is the [Aritificial Analysis's LLM Leaderboard](https://artificialanalysis.ai/leaderboards/models)

**Recommendations**:

- [Google Gemma 2](https://ollama.com/library/gemma2)
- [Meta Llama 3.1](https://ollama.com/library/llama3.1)
- [Alibaba Qwen2](https://ollama.com/library/qwen2)

#### Choose Parameter Size

The model size should be smaller than your memory size.

> For instance, the `gemma2:9b` model is 5.4GB which is runnable on devices with 16GB memory.
>
> However, the `gemma2:27b` model is 16GB and it is not runnable on the same device (there must be some other programs that eat up your memory).

### Drawbacks of Running in Terminal

Your chat history cannot be saved. If you want to store your history chat, deploy one of the following apps (the titles link to their GitHub Repos):

- [Enchanted (macOS Only)](https://github.com/AugustDev/enchanted)
- [Open WebUI](https://github.com/open-webui/open-webui)

## Enchanted

[Download in AppStore](https://apps.apple.com/gb/app/enchanted-llm/id6474268307)

## Open WebUI

1. Download [Docker](https://www.docker.com/)
2. Follow the [Instructions](https://github.com/open-webui/open-webui?tab=readme-ov-file#how-to-install-)

## MoA

[Together MoA Repo](https://github.com/togethercomputer/MoA)

> Mixture of Agents (MoA) is a novel approach that leverages the collective strengths of multiple LLMs to enhance performance, achieving state-of-the-art results.

![MoA](https://github.com/togethercomputer/MoA/blob/main/assets/moa-3layer.png?raw=true)

The original MoA does not support Ollama. Here is [my edited Ollama version of MoA](https://github.com/gitmichaelqiu/MoA-Ollama-Chat) forked from [severian42's MoA-Ollama-Chat](https://github.com/severian42/MoA-Ollama-Chat). I edited the GUI to make it look better.

Follow the [Instructions](https://github.com/gitmichaelqiu/MoA-Ollama-Chat) here.
