wbrp-django-template
====================

This is our custom Django project template at Webrepublic. It is based on the
Django 1.5.1 standard template.


Features
--------

Layout
~~~~~~

- The Django project itself is moved down one level into a separate folder
- Requirements are split up into several files
- The main app lives inside a folder called ``config``
- There is a default app for the frontend called ``front``.
- Tests should go into a ``tests`` subdirectory inside the apps and be named
  ``test*.py``.

Config
~~~~~~

- Admin is enabled by default
- ``SECRET_KEY`` and other configuration variables are read from env, instead of
  writing them into your settings file.
- There's a ``test.sh`` script in the project directory that runs all tests and
  shows coverage information afterwards.
- Database configuration is read from environment.
- Coverage configuration is inside ``{{ project_name }}/.coveragerc``.

Apps
~~~~

- `django-debug-toolbar`_
- `django-discover-runner`_
- `django-extensions`_
- `django-messagegroups`_
- `south`_


Usage
-----

Install Django::

    $ mkvirtualenv {{ project_name }}
    $ pip install "Django>=1.5,<1.6"

Create a new project::

    $ django-admin.py startproject {{ project_name }} \
        --template=https://github.com/wbrp/wbrp-django-template/archive/master.zip \
        --extension py,rst,sh
    $ cd {{ project_name }}

Install dependencies::

    $ pip install -r requirements/local.txt

Fix permissions::

    $ cd {{ project_name }}
    $ chmod +x test.sh manage.py

Set environment variables::

    $ POSTACTIVATE=$VIRTUAL_ENV/$VIRTUALENVWRAPPER_ENV_BIN_DIR/postactivate
    $ echo "export DJANGO_DEBUG=True" >> $POSTACTIVATE
    $ echo "export PORT=8000" >> $POSTACTIVATE
    $ echo "export DATABASE_URL='postgres://localhost/{{ project_name }}'" >> $POSTACTIVATE
    $ source $POSTACTIVATE

Initialize database::

    $ createdb {{ project_name }}
    $ ./manage.py syncdb --all
    $ ./manage.py migrate --fake

Test setup::

    $ ./test.sh

There should be one passing test. It is recommended that now you pin your
dependency versions in the requirements files.

.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
.. _django-discover-runner: https://github.com/jezdez/django-discover-runner
.. _django-extensions: https://github.com/django-extensions/django-extensions
.. _django-messagegroups: https://github.com/dbrgn/django-messagegroups
.. _django-social-auth: https://github.com/omab/django-social-auth
.. _south: http://south.aeracode.org/
