# research-fi-cms
Github repository for research.fi Content Management System

# Installation
```
cd django
python -m pip install --upgrade pip
pip install -r requirements.txt
```

# Local development
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