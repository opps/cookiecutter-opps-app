# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.widgets import OppsEditor
from opps.core.admin import PublishableAdmin, opps_apps_rules

from .models import {{cookiecutter.repo_name.title()}}


@apply_opps_rules('{{cookiecutter.repo_name}}')
class {{cookiecutter.repo_name.title()}}Admin(PublishableAdmin):
    """ {{cookiecutter.repo_name}} Admin """
    class Meta:
        model = {{cookiecutter.repo_name.title()}}


admin.site.register({{cookiecutter.repo_name.title()}}, {{cookiecutter.repo_name.title()}}Admin)
