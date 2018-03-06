imaque
------
Testing pyramid framework.


Getting Started
---------------

Change directory into project.
```
$ cd imaque
```

Create a Python virtual environment.
```
$ python3 -m venv venv
```

Upgrade packaging tools.
```
$ venv/bin/pip install --upgrade pip setuptools
```

Install the project in editable mode with its testing requirements.
```
$ venv/bin/pip install -e ".[testing]"
```

Run tests.
```
$ venv/bin/pytest
```

Run project (requires certain env variables).
```
$ make develop
```