#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    '''
    帖子表
    '''
    #标题最大长度255,不能重名
    title = models.CharField(u'文章标题',max_length=255,unique=True)
    #发布办款-使用外键关联Category
    category = models.ForeignKey("Category",verbose_name='板块名称')
    '''
    这里在admin中,title默认是显示英文的,我们可以在他的最前面加要给字段,在admin中就可以显示中文,他和verbose_name一样,什么时候必须使用
    verbose_name呢?比如上面的{category = models.ForeignKey("Category",verbose_name='板块名称')} 这个字段第一个字段是关联的类,这里
    就必须使用verbose_name
    '''
    #上传文件
#    head_img = models.ImageField(upload_to="uploads")
    #文章内容(文章内容可能有很多,所以我们就不用"CharField"来写了,我们用TextField,不用规定他多长了,为可扩展长度)
    content = models.TextField(u"内容")
    #文章作者
    author = models.ForeignKey("UserProfile",verbose_name="作者")
    #发布日期
    publish_date = models.DateTimeField(auto_now=True,verbose_name="发布日期")
    #是否隐藏
    hidden = models.BooleanField(default=False,verbose_name="是否隐藏")
    #帖子的优先级
    priority = models.IntegerField(default=1000,verbose_name="优先级")

    def __unicode__(self):
        return "<%s,author:%s>" % (self.title,self.author)

class Comment(models.Model):
    '''
    评论表
    '''
    #评论是基于文章的,并且一条评论只属于一个文章!对多的关系
    #一个文章可以有多个评论,一个评论只属于一个文章
    #评论文章
    article = models.ForeignKey("Article")
    #评论用户
    user = models.ForeignKey("UserProfile")
    #评论内容
    comment = models.TextField(max_length=1000)
    #评论时间
    date = models.DateTimeField(auto_now=True)

    #多级评论,是不是评论评论的当前的表(自己表),所以就得和自己做一个关联!
    #这里在关联自己的时候必须设置一个related_name否则会报错冲突
    #这里parent_comment,必须设置为可以为空,因为如果他是第一评论他是没有父ID的
    parent_comment = models.ForeignKey("self",related_name='p_comment',blank=True,null=True)
    '''
    prent self
    Null    1
      2
      3
      4
    通过上面的这种方法来记录,评论的级别关系!
    '''
    def __unicode__(self):
        return "<user:%s>" %(self.user)
class ThumbUp(models.Model):
    '''
    点赞
    '''
    #给那个文章点的
    article = models.ForeignKey('Article')
    #用户名
    user = models.ForeignKey('UserProfile')
    #时间
    date = models.DateTimeField(auto_now=True)


class Category(models.Model):
    '''
    板块表
    '''
    #板块名称
    name = models.CharField(max_length=64,unique=True,verbose_name="板块名称")
    #板块管理员
    admin = models.ManyToManyField("UserProfile",verbose_name="模块管理员")
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    '''
    用户表
    '''
    #使用Django提供的用户表,直接继承就可以了.在原生的User表里扩展!(原生的User表里就有用户名和密码)
    #一定要使用OneToOne,如果是正常的ForeignKey的话就表示User中的记录可以对应UserProfile中的多条记录!
    #并且OneToOne的实现不是在SQL级别实现的而是在代码基本实现的!
    user = models.OneToOneField(User)
    #名字
    name = models.CharField(max_length=32)
    #属组
    groups = models.ManyToManyField("UserGroup")

    def __unicode__(self):
        return self.name

class UserGroup(models.Model):
    '''
    用户组表
    '''
    name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.name
    