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

Config
~~~~~~

- Admin is enabled by default
- `SECRET_KEY` and other configuration variables are read from env, instead of
  writing them into your settings file.

Apps
~~~~

- ...


Usage
-----

::

    $ django-admin.py startproject <project_name> \
        --template=https://github.com/wbrp/wbrp-django-template/archive/master.zip
