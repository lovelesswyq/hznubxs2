from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class jobPublishedManager(models.Manager):
    def get_queryset(self):
        return super(jobPublishedManager,
                    self).get_queryset().filter(status='published')

# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #闁哄秴娲。锟�    
    title = models.CharField(max_length=250)
    #闁活収鍘介悥锝囩驳閹惧懐绀夊☉鎾虫惈缁楁锟芥稒鍔栭悗顖氼嚈缁☆枠Ls
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    #濞达絾绮忛敓鏂ゆ嫹
    author = models.ForeignKey(User,
                                related_name='job_jobs')
    #濞戞捁顔婄紞锟�
    body = models.TextField()
    #闁告瑦鍨电粩鐑藉籍閸洘锛�
    publish = models.DateTimeField(default=timezone.now)
    #闁告帗绋戠紓鎾诲籍閸洘锛�
    created = models.DateTimeField(auto_now_add=True)
    #闁哄洤鐡ㄩ弻濠囧籍閸洘锛�
    updated = models.DateTimeField(auto_now=True)
    #閻㈩垱鐗曢悺娆戜沪閺囩姰浠涢柣妯垮煐閿熸枻鎷�
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    tags = TaggableManager()

    #闁革负鍔嶈啯闁搞劌顑戠槐妾搊del闁挎稑顦懙鎴︽儍閸曨叀顫eta闁告牕鎳庨幆鍫ュ礂閸愨晜娈堕柟璇″枔閿熻棄鍊归崹婊勭椤掞拷閹诧紕鎷犳繅淇瞐ngo闁哄被鍎撮妤呭极閻楀牆绁﹂幖瀛樻尵濞堟垿寮捄鐚存嫹閿燂拷
    #濮掓稒顭堥缁樻交閺傛寧绀�闁汇劌瀚Σ鎼佸冀鐟欏嫬绁ublish閻庢稒顨嗛灞炬交濞戞粠鏀介梻鍕Т缁參骞掗幒鎴濈仚閺夆晛娲ㄥ▓鎴犵磼閹惧浜柕鍡楀�归崹婊勭椤戝灝鈻忛柣鈧姀缁�瀣矗闁垮闄嶉柟绋挎搐閻ｏ拷
    #閺夆晜绋栭、鎴︽⒔瀹ュ懐纰嶉柟鐑樺笒閸亪濡撮敓锟�
    
    class Meta:
           ordering = ('-publish',)
    #*str()*闁哄倽顫夌涵鍫曞及椤栨氨绉奸柛鎾崇Т椤曨喚鎸掗敓鐘靛笡閻犱降鍊楀▓鎴﹀矗椤栨繍鍤㈤悶娑栧妿楠炲洭濡撮敓锟�
    #Django閻忓繐妫旂槐浼村捶閵娿儳鍙戝鑸佃壘濠�鎾棘閸︻厽鏆忛柛鎺撴緲閻ｇ姵绗熺�ｎ亶娲ょ紒鐙呯磿閹﹦绮╁▎鎴濅化濞戞搩鍘归敓鏂ゆ嫹
    def __str__(self):
        return self.title
    
    objects = models.Manager() # The default manager.
    published = jobPublishedManager() # Our custom manager.
    
    def get_absolute_url(self):
        return reverse('job:job_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
    #閻犲洭鏀遍弫鐐哄箛韫囥儳绀夐柟瀛樺灣濠婃垿鏌呭宕囩畺濞达綀娉曢弫顦檛rftime()闁哄倽顫夌涵鍫曞级閵夈倗绠介悹鍥︽闁叉粍鎷呭鍡樻闁汇劌瀚﹢锟藉ù鐘烘閹蜂即寮妷锔藉焸
    #闂傚浄鎷烽悷鏇氱閻㈩偅绋夐敓锟�0闁哄鍎查悗顖氼嚈缁☆枠L*闁靛棗鍊归崹婊勭椤掞拷閻ㄣ垺瀵煎顒佽含闁瑰瓨鍨冲鎴︽儍閸曨儫渚�寮堕崠锛勭templates闁挎稑顦懙鎴炴媴閿燂拷
    #闁烩懇鏆巈t_absolute_url()*闁哄倽顫夌涵鍫曞Υ閿燂拷
    

class jobComment(models.Model):
    post = models.ForeignKey(Job, related_name='comments')
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

