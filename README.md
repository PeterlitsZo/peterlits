Peterlits api README
===============================================================================

this is the project for api.peterlits.com

Setup
-------------------------------------------------------------------------------

1. download `python3`, `pip3` and `virtualenv`.

2. Firstly, you need to setup the virtualenv at `./venv`. (Or other paths, but
then you need to change the `VENV`). We set `VENV` to be `./venv`.

3. then you need to run `source ${VENV}/bin/activate` to set the environment
vairable, and then run `make install` to install all python-lib/module for this
project.

4. write `./peterlits_api/peterlits_api/private.py` like:
```python
SECRET_KEY = '<the secret key of yourself>'
DEBUG = False # because the private.py is not hold by git, so you can set it as
              # True if you like and needn't wrroy it will break the file online.
```


