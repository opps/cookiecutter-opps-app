# coding:utf-8

from django.conf.urls import patterns, url

from .views import {{cookiecutter.repo_name.title()}}Detail


urlpatterns = patterns(
    "",
    url(
      r'',
      {{cookiecutter.repo_name.title()}}Detail.as_view(),
      name='detail_{{cookiecutter.repo_name}}'
    ),
)
