from django.shortcuts import render
from index.models import ArticleColumn
from django.core.cache import cache
from .models import About_models
# Create your views here.

# @cache_page(10 * 60)
def about_me(request):
    if cache.has_key("classify"):
        classify = cache.get("classify")
    else:
        # 获取所有的文章分类（分类缓存一天）
        classify = ArticleColumn.objects.all()
        cache.set("classify", classify, 24*60*60)
    # 关于部分缓存
    if cache.has_key("about_parts"):
        about_parts = cache.get("about_parts")
    else:
        # 获取所有的文章分类（分类缓存一天）
        about_parts = About_models.objects.all()
        cache.set("about_parts", about_parts, 24 * 60 * 60)
    context = {"classify": classify, "about_parts": about_parts}
    return render(request, 'about/about.html', context=context)