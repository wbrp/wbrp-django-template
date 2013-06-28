# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'front/home.html'
