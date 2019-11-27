from django.db import models
# Create your models here.
from index.models import ArticlePost
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
# 引入富文本编辑器
from ckeditor.fields import RichTextField

class Comments(MPTTModel):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    # 新增，mptt树形结构
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='children')

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='replyers')

    # class Meta:
    #     ordering = ('created',)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]