# Tuto Flask

[**Miguel Grinberg's** tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) on getting the grips with [*Flask*](http://flask.pocoo.org/).

## Setup

The following assumes Python 3.4 is used.

Under FC21, the Python package `virtualenv` is offered if not already installed:
```
bash: virtualenv: command not found...
Install package 'python-virtualenv' to provide command 'virtualenv'? [N/y]
```

Python 3 oblige some commands must be changed:
```
$ mkdir microblog_part_xxx
$ cd microblog_part_xxx
$ virtualenv --python=python3.4 flask
$ . flask/bin/activate
```
The required packages can now be installed in the virtual environment:
```
$ flask/bin/pip install flask
```

## Notes

Use the `deactivate` command to exit the virtual environment.
