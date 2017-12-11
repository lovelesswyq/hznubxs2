# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
urlpatterns = [
    # post views
    url(r'^$', views.unuse_list, name='unuse_list'),
    # url(r'^$', views.PostListView.as_view(),name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.unuse_list,
    name='unuse_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.unuse_detail,
        name='unuse_detail'),
    url(r'^bbs_pub$',views.contact),
]

