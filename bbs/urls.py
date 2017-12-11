# coding=utf-8
from django.conf.urls import include,url
from django.contrib import admin
from app import views
from app import urls
from django.contrib.auth.views import login
import app
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'bbs_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    # 配置url
    url(r'^admin/', admin.site.urls),
 
    # 登陆页面url
    url(r'^login/$', login, name='login'),
    url(r'^login/$', views.Login ),
    url(r'^acc_login/$', views.acc_login),
    url(r'^logout/$', views.logout_view),
    url(r'^account/',include('account.urls')),    
    url(r'', include(app.urls)),
    url(r'^blog/', include('blog.urls',
        namespace='blog',
        app_name='blog')),
    url(r'^travel/', include('travel.urls',
        namespace='travel',
        app_name='travel')),
    url(r'^unuse/', include('unuse.urls',
        namespace='unuse',
        app_name='unuse')),
    url(r'^study/', include('study.urls',
        namespace='study',
        app_name='study')),
    url(r'^job/', include('job.urls',
        namespace='job',
        app_name='job')),
]