# MLTabularPipelines

MLTabularPipelines `mltabpipe` is a workshop of modualized machine learning pipelines for tabular tasks.

This project aims to simplify the procedure of training models as you probably should put more time on other tasks such as Feature Engineering. This can also help begineers to get familiar with the procedures of completing a Data Science project.

It is available at [GitHub](https://github.com/gitmichaelqiu/MLTabularPipelines).

## Installation

Simply put `mltabpipe` folder into your project directory. You may use it by:

```python
from mltabpipe.ensemble import gbdt
```

MLTabularPipelines enables GPU/CUDA by default. Make sure you have installed GPU versions for acceleration. This, however, is not a requirement. You may still train with CPU.

## Update

There is an interal update checker integrated in `mltabpipe`. It will check for new releases when you import any modules. Each check has an interval no shorter than 24 hours. When new update is available, for compatibility, you should not directly replace the folder. Use it for your new projects.

## License

The project MlTabularPipelines is under the terms of the MIT License. Use it as you want.
