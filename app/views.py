# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from app import models
from django.contrib.contenttypes.models import ContentType
 
 
 
# Create your views here.
 
# 创建登陆视图
def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    print(username, password)
    if user is not None:
        auth.login(request, user)
        content = '''
        Welcome %s !!!
 
        <a href='/logout/' >Logout</a>
 
         ''' % user.username
        #return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
 
def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return render_to_response('registration/logged_out.html')

#    return HttpResponse("<b>%s</b> logged out! <br/><a href='/login/'>Re-login</a>" % user)
 
def Login(request):
    return render_to_response('login.html')

def login(request):
    return render_to_response('login.html')

def index(request):
    # 从数据库中取出bbs数据渲染到index.html中
    bbs_list = models.Article.objects.all()
    # 取出bbs的类别
    bbs_categories = models.Category.objects.all()
    return render_to_response('/account/dashboard.html', {'bbs_list': bbs_list,
                                             'user': request.user,  # 将登陆认证后的信息返回
                                             'bbs_category': bbs_categories,
                                             'bbs_id': 0,
                                              })
 
 
 
# bbs分类
def category(request, cate_id):
    bbs_list = models.BBS.objects.filter(category__id=cate_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html', {'bbs_list': bbs_list,
                                             'user': request.user,
                                             'bbs_category': bbs_categories,
                                             'bbs_id': int(cate_id),
                                              })
 
# bbs的详细介绍
def bbs_detail(request, bbs_id):
    # 取出bbs_id下的详细内容
    bbs = models.BBS.objects.get(id=bbs_id)
 
    return render_to_response('bbs_detail.html', {'bbs_obj': bbs,
                                                  'user': request.user})
 
 
# 添加评论
 
def sub_comment(request):
    print(request.POST)
    bbs_id = request.POST.get('bbs_id')
 
    comment = request.POST.get('comment_content')
 
    comments.models.Comment.objects.create(
        content_type_id=7,  # bbs表在数据库中的id号
        object_pk=bbs_id,
        site_id=1,
        user_id=request.user.id,    # 这里与源代码不同 如果不加.id，会出现int() argument must be a string or a number, not ‘SimpleLazyObject’错误
        comment=comment,
    )
    #重定向
 
    return HttpResponseRedirect('/detail/%s'% bbs_id)
 
def bbs_pub(request):
    return render_to_response('bbs_pub.html')
 
 
def bbs_sub(request):
    print(request.POST.get('content'))
    title = request.POST.get('title')
    content = request.POST.get('content')
    summary = request.POST.get('summary')
    author = models.BBS_user.objects.get(user__username=request.user)
    models.BBS.objects.create(
        title=title,
        summary=summary,
        content=content,
        author=author,
        view_count=1,
        ranking=1,
        #created_at=models.DateTimeField(auto_now_add=True),  # 创建日期
        #updated_at = models.DateTimeField(auto_now_add=True),  # 修改日期
    )
    return HttpResponse("<h2>Bbs was published, please enter <br/><a href='/'>return</a> to index!<h2>")
