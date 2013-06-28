#!/bin/bash
cd {{ project_name }}
coverage run manage.py test $1 \
&& echo \
&& coverage report \
&& rm .coverage
