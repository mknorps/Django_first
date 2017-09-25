# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# File name: urls.py
# Created by: gemusia
# Creation date: 25-09-2017
# Last modified: 25-09-2017 11:10:27
# Purpose: 
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'index')
]


