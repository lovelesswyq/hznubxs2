from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class travelPublishedManager(models.Manager):
    def get_queryset(self):
        return super(travelPublishedManager,
                    self).get_queryset().filter(status='published')

# Create your models here.
class Travel(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #閺嶅洭顣�    
    title = models.CharField(max_length=250)
    #閻厽鐖ｇ粵鎾呯礉娑撳搫绗樼�涙劖鐎绡Ls
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    #娴ｆ粏锟斤拷
    author = models.ForeignKey(User,
                                related_name='travel_travels')
    #娑撹缍�
    body = models.TextField()
    #閸欐垵绔烽弮鍫曟？
    publish = models.DateTimeField(default=timezone.now)
    #閸掓稑缂撻弮鍫曟？
    created = models.DateTimeField(auto_now_add=True)
    #閺囧瓨鏌婇弮鍫曟？
    updated = models.DateTimeField(auto_now=True)
    #鐢牕鐡欑仦鏇犮仛閻樿埖锟斤拷
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    tags = TaggableManager()

    #閸︺劍膩閸ㄥ绱檓odel閿涘鑵戦惃鍕Meta閸栧懎鎯堥崗鍐╂殶閹诡喓锟藉倹鍨滄禒顒�鎲＄拠濉俲ango閺屻儴顕楅弫鐗堝祦鎼存挾娈戦弮璺猴拷锟�
    #姒涙顓绘潻鏂挎礀閻ㄥ嫭妲搁弽瑙勫祦publish鐎涙顔屾潻娑滎攽闂勫秴绨幒鎺戝灙鏉╁洨娈戠紒鎾寸亯閵嗗倹鍨滄禒顑垮▏閻€劏绀嬮崣閿嬫降閹稿洤鐣�
    #鏉╂稖顢戦梽宥呯碍閹烘帒鍨妴锟�
    
    class Meta:
           ordering = ('-publish',)
    #*str()*閺傝纭堕弰顖氱秼閸撳秴顕挒锟犵帛鐠併倗娈戦崣顖濐嚢鐞涖劎骞囬妴锟�
    #Django鐏忓棔绱伴崷銊ョ发婢舵艾婀撮弬鍦暏閸掓澘鐣犳笟瀣洤缁狅紕鎮婄粩娆戝仯娑擃厹锟斤拷
    def __str__(self):
        return self.title
    
    objects = models.Manager() # The default manager.
    published = travelPublishedManager() # Our custom manager.
    
    def get_absolute_url(self):
        return reverse('travel:travel_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
    #鐠囬攱鏁為幇蹇ョ礉閹存垳婊戦柅姘崇箖娴ｈ法鏁trftime()閺傝纭堕弶銉ょ箽鐠囦椒閲滄担宥嗘殶閻ㄥ嫭婀�娴犺棄鎷伴弮銉︽埂
    #闂囷拷鐟曚礁鐢稉锟�0閺夈儲鐎绡L*閵嗗倹鍨滄禒顒�鐨㈡导姘躬閹存垳婊戦惃鍕侀弶鍖＄礄templates閿涘鑵戞担锟�
    #閻⑩暎et_absolute_url()*閺傝纭堕妴锟�
    

class travelComment(models.Model):
    post = models.ForeignKey(Travel, related_name='comments')
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

