#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin
from app import models
# Register your models here.

#给某个表专门的定制的类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','hidden','publish_date')

admin.site.register(models.Article,ArticleAdmin) #把自定义的类绑定到注册的类中
admin.site.register(models.Category,CategoryAdmin)  #把自定义的类绑定到注册的类中
admin.site.register(models.Comment)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)