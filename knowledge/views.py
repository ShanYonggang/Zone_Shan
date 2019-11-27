from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import MyKnowledgeUrl, MyBookShare, MySoftware
# 引入缓存包
from django.views.decorators.cache import cache_page
# 引入缓存
from django.core.cache import cache
from index.models import ArticleColumn
# Create your views here.
@cache_page(10*60)
def get_knowledge(request):
    if cache.has_key("classify"):
        classify = cache.get("classify")
    else:
        # 获取所有的文章分类（分类缓存一天）
        classify = ArticleColumn.objects.all()
        cache.set("classify", classify, 24*60*60)
    urls = MyKnowledgeUrl.objects.all()
    books = MyBookShare.objects.all()
    softwares = MySoftware.objects.all()
    context = {'urls': urls, 'books': books, 'softwares': softwares, "classify": classify}
    return render(request, 'knowledge/knowledge.html', context=context)
    # return HttpResponse("这是显示资料的页面！！！")