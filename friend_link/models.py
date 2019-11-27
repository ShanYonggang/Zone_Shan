from django.db import models

# Create your models here.
class FriendLink(models.Model):
    # 怎么称呼您
    name = models.CharField(max_length=20, verbose_name='称呼')
    # 友情链接url
    friend_url = models.URLField(verbose_name='链接地址')
    # 友情链接显示名称
    website_name = models.CharField(max_length=20, verbose_name='网站名称')
    # 邮箱地址
    your_email = models.EmailField(verbose_name='友情链接邮箱(为您保密)')
    # 上传图片
    url_image = models.ImageField(upload_to='link/%Y%m%d/', verbose_name='网站代表图片', blank=True)
    # 提交时间
    submit_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['submit_time']
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'