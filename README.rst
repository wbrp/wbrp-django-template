wbrp-django-template
====================

This is our custom Django 1.7 project template at Webrepublic.


Features
--------

Layout
~~~~~~

- The Django project itself is moved down one level into a separate folder
- Requirements are split up into several files
- The main app lives inside a folder called ``config``
- There is a default app for the frontend called ``front``.
- Tests should go into a ``tests`` subdirectory inside the apps and be named
  ``test_*.py``.

Config
~~~~~~

- Admin is enabled by default
- ``SECRET_KEY`` and other configuration variables are read from env, instead of
  writing them into your settings file.
- Database configuration is read from environment.

Auth
~~~~

- Authentication is done via python-social-auth_.
- By default, Google OAuth2 is enabled, but without offline access. If you want
  offline access, comment out the
  ``SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS`` line in your
  ``settings.py``.
- To enable additional OAuth2 scopes, edit ``SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_SCOPE``.
- To limit login to people from a specific domain, add them to
  ``SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS``.

Testing
~~~~~~~

- Testing is set up using pytest_.
- You can use the ``runtests.py`` script to run all tests and show coverage
  information afterwards.
- PEP8 violations in the project directory (excluding tests and migrations) are
  counted as errors. PEP8 errors E126, E127 and E128 are ignored. Max line
  length is set to 99 characters.
- Coverage configuration is at ``{{ project_name }}/.coveragerc``.
- Pytest configuration is at ``{{ project_name }}/pytest.ini``.
- To speed up tests, you can use the ``--reuse-db`` option to avoid destroying
  the database after a test run. Don't use this option after model changes,
  otherwise tests will fail.

Apps
~~~~

- django-debug-toolbar_
- django-extensions_
- django-messagegroups_
- python-social-auth_
- pytest_
- pytest-django_
- pytest-cov_
- pytest-pep8_


Usage
-----

Install Django::

    mkvirtualenv {{ project_name }}
    pip install "Django>=1.7,<1.8"

Create a new project::

    django-admin.py startproject {{ project_name }} \
      --template=https://github.com/wbrp/wbrp-django-template/archive/master.zip \
      --extension py,rst,ini
    cd {{ project_name }}

Install dependencies::

    pip install -r requirements/dev.txt

Fix permissions::

    cd {{ project_name }}
    chmod +x manage.py runtests.py

Set environment variables::

    POSTACTIVATE=$VIRTUAL_ENV/$VIRTUALENVWRAPPER_ENV_BIN_DIR/postactivate
    echo "export DJANGO_DEBUG=True" >> $POSTACTIVATE
    echo "export PORT=8000" >> $POSTACTIVATE
    echo "export DATABASE_URL='postgres://localhost/{{ project_name }}'" >> $POSTACTIVATE
    echo "export GOOGLE_OAUTH2_CLIENT_KEY='<client_key>'" >> $POSTACTIVATE
    echo "export GOOGLE_OAUTH2_CLIENT_SECRET='<client_secret>'" >> $POSTACTIVATE
    source $POSTACTIVATE

Initialize database::

    createdb {{ project_name }}
    ./manage.py migrate

Test setup::

    ./runtests.py
    ./manage.py runserver

There should be at least two passing test (and no fails). It is recommended that
now you pin your dependency versions in the requirements files.

.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
.. _django-extensions: https://github.com/django-extensions/django-extensions
.. _django-messagegroups: https://github.com/dbrgn/django-messagegroups
.. _python-social-auth: https://github.com/omab/python-social-auth
.. _pytest: http://pytest.org/
.. _pytest-django: http://pytest-django.readthedocs.org/
.. _pytest-cov: https://bitbucket.org/memedough/pytest-cov/overview
.. _pytest-pep8: https://bitbucket.org/hpk42/pytest-pep8
