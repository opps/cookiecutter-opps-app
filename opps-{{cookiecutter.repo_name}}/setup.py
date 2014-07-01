# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from opps import {{cookiecutter.repo_name}}


install_requires = ["opps"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Opps",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except:
    long_description = {{cookiecutter.repo_name}}.__description__

setup(
    name='opps-{{cookiecutter.repo_name}}',
    namespace_packages=['opps', 'opps.{{cookiecutter.repo_name}}'],
    version={{cookiecutter.repo_name}}.__version__,
    description={{cookiecutter.repo_name}}.__description__,
    long_description=long_description,
    classifiers=classifiers,
    keywords='{{cookiecutter.repo_name}} opps cms django apps magazines websites',
    author={{cookiecutter.repo_name}}.__author__,
    author_email={{cookiecutter.repo_name}}.__email__,
    url='http://oppsproject.org',
    download_url="https://github.com/opps/opps-{{cookiecutter.repo_name}}/tarball/master",
    license={{cookiecutter.repo_name}}.__license__,
    packages=find_packages(exclude=('doc', 'docs',)),
    package_dir={'opps': 'opps'},
    install_requires=install_requires,
    include_package_data=True,
    package_data={
        '{{cookiecutter.repo_name}}': ['templates/*']
    }
)
