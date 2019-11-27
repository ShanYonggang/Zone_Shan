from django.shortcuts import render
from . import models
import markdown
from index.models import ArticleColumn
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
def development(request):
    if cache.has_key("classify"):
        classify = cache.get("classify")
    else:
        # 获取所有的文章分类
        classify = ArticleColumn.objects.all()
        cache.set("classify", classify, 60*60)
    #  网站更新信息缓存
    if cache.has_key("news_list"):
        news_list = cache.get("news_list")
    else:
        news_list = []
        new_list = models.Development.objects.all().order_by('story_time')
        for news in new_list:
            news_list.append(news)
        cache.set("news_list", news_list, 60 * 60)
    context = {
        'news_list': news_list,
        "classify": classify,
    }
    return render(request, 'story/story.html', context=context)