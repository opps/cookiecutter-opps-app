#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pkg_resources

pkg_resources.declare_namespace(__name__)

VERSION = (0, 1, 0)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"{{cookiecutter.repo_name}} App for Opps CMS"

__author__ = u"{{cookiecutter.author}}"
__credits__ = []
__email__ = u"{{cookiecutter.email}}"
__license__ = u"{{cookiecutter.license}}"
__copyright__ = u"Copyright {{cookiecutter.year}}, {{cookiecutter.author}}"
