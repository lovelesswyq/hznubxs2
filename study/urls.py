# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
urlpatterns = [
    # post views
    url(r'^$', views.study_list, name='study_list'),
    # url(r'^$', views.PostListView.as_view(),name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.study_list,
    name='study_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.study_detail,
        name='study_detail'),
    url(r'^bbs_pub$',views.contact),
]

