<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-postgres-matviews-commands.svg?longCache=True)](https://pypi.org/project/django-postgres-matviews-commands/)
[![](https://img.shields.io/pypi/v/django-postgres-matviews-commands.svg?maxAge=3600)](https://pypi.org/project/django-postgres-matviews-commands/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-postgres-matviews-commands.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-postgres-matviews-commands.py/)

#### Installation
```bash
$ [sudo] pip install django-postgres-matviews-commands
```

#### Settings
```python
INSTALLED_APPS = [
    ...
    'django_postgres_matviews_commands',
    ...
]
```

#### Examples
dev
```bash
$ python manage.py refresh_matviews
$ python manage.py drop_matviews
```

prod
```bash
$ ssh user@hostname sudo docker run --env-file .env image python manage.py refresh_matviews
$ ssh user@hostname sudo docker run --env-file .env image python manage.py drop_matviews
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>