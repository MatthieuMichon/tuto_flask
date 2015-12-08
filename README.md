# Tuto Flask

[**Miguel Grinberg's** tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) on getting the grips with [*Flask*](http://flask.pocoo.org/).

## Setup

The following assumes Python 3.4 is used.

Under FC21, the Python package `virtualenv` is offered if not already installed:
```
bash: virtualenv: command not found...
Install package 'python-virtualenv' to provide command 'virtualenv'? [N/y]
```

Python 3 oblige `pip` now becomes `pip3`:
```
flask/bin/pip3 install flask
```

## Notes

Before running the server, the virtual environment must be activated:
```
$ . flask/bin/activate
$ ./run.py
```
Use the `deactivate` command to exit the virtual environment.
