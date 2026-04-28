# blog

This is my blog site, built with [Zensical](https://github.com/zensical/zensical) and licensed under [MIT License](./LICENSE).

Visit [here](https://gitmichaelqiu.github.io/blog).

## Build This Site Locally

```bash
git clone https://github.com/gitmichaelqiu/blog.git
cd blog
zensical build
```

This site uses a hybrid approach for building the site. An extra python script is used to pre-render the site.

```bash
./build.sh
cd site
python -m http.server
```
