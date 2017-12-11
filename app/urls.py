from django.conf.urls import url
 
from app import views
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'bbs_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^$', views.index),
    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^sub_comment/$', views.sub_comment),
    url(r'^bbs_pub/$', views.bbs_pub),
    url(r'^bbs_sub/$', views.bbs_sub),
    url(r'^category/(\d+)', views.category),
]