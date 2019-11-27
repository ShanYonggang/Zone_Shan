from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    # 创建时间
    c_time = models.DateTimeField(auto_now_add=True)
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True)
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 个人网站
    your_url = models.URLField(verbose_name='个人网站', blank=True)
    # 微信号
    wechat = models.CharField(max_length=20, blank=True)
    # QQ号
    QQ_num = models.CharField(max_length=20, blank=True)
    # 昵称
    nickname = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

