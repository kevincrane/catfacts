# Django settings for catfactssite project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'catfacts_db',                  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

HOSTNAME = 'http://localhost:8000'

# Additional locations of static files
STATICFILES_DIRS = (
    "/home/kevin/workspace/catfactssite/static",
    )

TEMPLATE_DIRS = (
    "/home/kevin/workspace/catfactssite/templates",
    )