wbrp-django-template
====================

This is our custom Django project template at Webrepublic. It is based on the
Django 1.5.1 standard template.


Features
--------

Layout
~~~~~~

- The Django project itself is moved down one level into a separate folder
- The main app lives inside a folder called ``config``
- Requirements are split up into several files
- Tests should go into a `tests` subdirectory inside the apps and be named
  `test*.py`.

Config
~~~~~~

- Admin is enabled by default
- `SECRET_KEY` and other configuration variables are read from env, instead of
  writing them into your settings file.
- There's a `test.sh` script in the root directory that runs all tests and
  shows coverage information afterwards.

Apps
~~~~

- `django-debug-toolbar`_
- `django-discover-runner`_
- `django-extensions`_
- `south`_


Usage
-----

Create a new project::

    $ django-admin.py startproject <project_name> \
        --template=https://github.com/wbrp/wbrp-django-template/archive/master.zip \
        --extension py,rst,sh

Fix permissions::

    $ chmod +x <project_name>/manage.py

Install dependencies::

    $ pip install -r requirements/local.txt


.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
.. _django-discover-runner: https://github.com/jezdez/django-discover-runner
.. _django-extensions: https://github.com/django-extensions/django-extensions
.. _south: http://south.aeracode.org/
