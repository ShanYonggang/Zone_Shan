from django import forms
from . import models

# 写文章的类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = models.ArticlePost
        fields = ('title','body','tags')
