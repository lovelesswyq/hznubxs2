from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #标题
    title = models.CharField(max_length=250)
    #短标签，为帖子构建URLs
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    #作者
    author = models.ForeignKey(User,
                                related_name='blog_posts')
    #主体
    body = models.TextField()
    #发布时间
    publish = models.DateTimeField(default=timezone.now)
    #创建时间
    created = models.DateTimeField(auto_now_add=True)
    #更新时间
    updated = models.DateTimeField(auto_now=True)
    #帖子展示状态
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    tags = TaggableManager()

    #在模型（model）中的类Meta包含元数据。我们告诉Django查询数据库的时候
    #默认返回的是根据publish字段进行降序排列过的结果。我们使用负号来指定
    #进行降序排列。
    
    class Meta:
           ordering = ('-publish',)
    #*str()*方法是当前对象默认的可读表现。
    #Django将会在很多地方用到它例如管理站点中。
    def __str__(self):
        return self.title
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
    #请注意，我们通过使用strftime()方法来保证个位数的月份和日期
    #需要带上0来构建URL*。我们将会在我们的模板（templates）中使
    #用get_absolute_url()*方法。
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

