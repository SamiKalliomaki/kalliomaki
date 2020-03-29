# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]