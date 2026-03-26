# Set up Environment

This guides will teach you how to set up a Machine Learning environment with conda and VSCode.

## Conda

Conda is a package manager for Python. It is a free and open source software that is used to install, update, and remove packages. It is also used to create and manage virtual environments.

### Installation

Go to [Anaconda](https://www.anaconda.com/download) and download the installer for your operating system. Then follow the installation instructions.

After completion, open your terminal and run this command to verify installation:

```bash
conda --version
```

### Create Virtual Environment

We create virtual environment because it allows us to isolate dependencies for different types of projects we want to work on. I suggest Python 3.11 for Machine Learning projects as most packages you will need are compatible with this version. Let us create an environment called `ml`:

```bash
conda create -n ml python=3.11
```

After creation, we need to activate the environment:

```bash
conda activate ml
```

Now you will see `(ml)` at the beginning of your terminal prompt, which indicates that the environment is activated. To deactivate the environment, run this command:

```bash
conda deactivate
```

### Install Packages

We use `pip` to install packages in conda environment. This [environment.yml](https://raw.githubusercontent.com/gitmichaelqiu/blog/main/docs/data-science/environment.yml) contains packages that I have been using. To install it, run this command:

```bash
conda env update --file environment.yml
```

Make sure you are already in `ml` environment before running the command!

## VSCode

In fact, you can choose what ever IDE you like, such as PyCharm. My preference is VSCode as it is free and simple. You can download it from [here](https://code.visualstudio.com/).

### Install Extensions

We commonly use Jupyter notebook for Machine Learning projects. So we need to install the Jupyter extension for VSCode. You can install it from [here](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

### Your First Jupyter Notebook

Create a file named `test.ipynb` and open it in VSCode. Create a new cell, set the language to Python, and add this command:

```python
print("Hello World!")
```

Click Run All at the top left bar, and the editor will ask you to select an intepreter. Choose the `ml` environment we created earlier. The run should be successful.

## Last

Welcome to the world of Data Science! In fact, I would say that I am pretty much a beginner at least when I am writing this post. I am excited to share my journey with you. Hopefully, you should see that each post is a step forward for myself. Let's start learning!

Remember, Data Science is not easy. It takes time and effort to learn (and also for your model to learn lol). It is a relatively new domain and the resources for learners may not be as systematic as other subjects. You may also stuck at some phases, just like how I kinda stuck at top 10% on Kaggle competitions. But always be optimistic and try your best! I promise you that this would be fun!
