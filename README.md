<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-postgres-matviews-commands.svg?maxAge=3600)](https://pypi.org/project/django-postgres-matviews-commands/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-postgres-matviews-commands.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-postgres-matviews-commands.py/actions)

### Installation
```bash
$ [sudo] pip install django-postgres-matviews-commands
```

##### `settings.py`
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
    <a href="https://readme42.com/">readme42.com</a>
</p>