# GitPop2

Find the most popular fork on GitHub <http://gitpop2.herokuapp.com/>

See <https://andremiras.github.io/gitpop3/> ([AndreMiras/gitpop3](https://github.com/AndreMiras/gitpop3)) for a rewrite using ReactJS.

[![tests](https://github.com/AndreMiras/gitpop2/workflows/tests/badge.svg)](https://github.com/AndreMiras/gitpop2/actions?query=workflow%3Atests)

GitPop2 helps you choose a fork when a project goes unmaintained. It allows you to sort forks by "stars count", "forks count" and "last update".

![Screenshot](https://raw.github.com/AndreMiras/gitpop2/master/docs/screenshot.png)

This project actually started as a "fork" of [jpmckinney/gitpop](https://github.com/jpmckinney/gitpop), because the site running the project went down in March 2014.
It's not a fork as defined by GitHub because it was started from scratch using a different web framework.

## Install
```sh
pip install -r requirements.txt
```

## Run
With Gunicorn WSGI server:
```sh
gunicorn gitpop2.wsgi
```
With Django development server:
```sh
python manage.py runserver
```
