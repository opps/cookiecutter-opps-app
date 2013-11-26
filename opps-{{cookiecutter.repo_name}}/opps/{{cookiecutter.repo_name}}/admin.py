# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.widgets import OppsEditor
from opps.core.admin import PublishableAdmin
from opps.core.admin import apply_opps_rules

from .models import {{cookiecutter.repo_name.title()}}



@apply_opps_rules('{{cookiecutter.repo_name}}')
class {{cookiecutter.repo_name.title()}}Admin(PublishableAdmin):
    """ {{cookiecutter.repo_name}} Admin """


admin.site.register({{cookiecutter.repo_name.title()}}, {{cookiecutter.repo_name.title()}}Admin)
