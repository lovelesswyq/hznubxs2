# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
urlpatterns = [
    # post views
    url(r'^$', views.job_list, name='job_list'),
    # url(r'^$', views.PostListView.as_view(),name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.job_list,
    name='job_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.job_detail,
        name='job_detail'),
    url(r'^bbs_pub$',views.contact),
]

