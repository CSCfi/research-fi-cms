# research-fi-cms

Github repository for research.fi Content Management System

# Local development
## Docker compose
```
docker-compose up
```
* Docker compose does the following
  * Launch the Django app in a Python container
  * Django source code directory is mapped to the container
  * Launch PostgreSQL database
    * Create database for Django app
    * Create database user
    * Database is persisted in a volume
## How to restore backup
* Check from docker-compose.yml which local directory is mapped as "/cmsvolume" in Django container. For now let's assume it is "/tmp"
* Create a subdirectory "dbbackup": /tmp/dbbackup
* Copy backup files into /tmp/dbbackup, for example
  * cms-2023-02-06-040500.tar.gz
  * default-cms-2023-02-06-040000.psql.gz
* Log into Django container
* Restore database
  * python manage.py dbrestore -z -s cms
* Restore media
  * python manage.py mediarestore -z -s cms
## Local settings

By default the app uses production settings and PostgreSQL database engine.
For local development add a settings file overriding settings.py values

```
django/cms/local_settings.py
```

Example content

```
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True
STATIC_URL = "static/"
STATIC_ROOT = "static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
```

# Developer notes

MyData content is handled with Page model. All MyData content should have page id with prefix "mydata\_". API endpoint for /mydata filters content according to this prefix.
