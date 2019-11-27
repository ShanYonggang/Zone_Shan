from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# 引入Q对象
from django.db.models import Q
# 引入评论模块
from comments.models import Comments
# 引入友情链接模块
from friend_link.models import FriendLink
from django.views.decorators.csrf import csrf_exempt
# 导入ip地址包
from ipware.ip import get_ip
import re, requests
# 引入缓存包
from django.views.decorators.cache import cache_page
# 引入缓存
from django.core.cache import cache
# 引入评论表单
from comments.forms import CommentForm

# Create your views here.
def roots(request):
    f = 'e95d2f4a675fe6f2ef2b098d2ae0d93e8c574ba1ff2bfa05'
    return HttpResponse(f)

# 博客主页
def blog_list(request):
    # 获取文章分类参数
    column = request.GET.get('column_id')
    # 获取标签参数
    tag = request.GET.get('tag')
    # 选取不同的排序方式
    order = request.GET.get('order')
    # 友情列表缓存
    if cache.has_key("friend_link"):
        friend_link = cache.get("friend_link")
    else:
        # 获取友情列表
        friend_link = FriendLink.objects.all().order_by('-submit_time')
        cache.set("friend_link", friend_link, 24 * 60 * 60)
    # 热门文章，加缓存
    if cache.has_key('five_articles_hot'):
        five_articles = cache.get('five_articles_hot')
    else:
        five_articles = models.ArticlePost.objects.all().order_by('-article_view')
        if five_articles.count() > 5:
            five_articles = five_articles[:5]
        else:
            five_articles = five_articles[:]
        cache.set('five_articles_hot', five_articles, 24 * 60 * 60)
    # 最新发表文章，加缓存
    if cache.has_key('five_articles_new'):
        five_new_articles = cache.get('five_articles_new')
    else:
        five_new_articles = models.ArticlePost.objects.all().order_by('-create_time')
        if five_new_articles.count() > 5:
            five_new_articles = five_new_articles[:5]
        else:
            five_new_articles = five_new_articles[:]
        cache.set('five_articles_new', five_new_articles, 24 * 60 * 60)
    # 选取不同的排序方式
    if cache.has_key('articles_all'):
        articles = cache.get('articles_all')
    else:
        articles = models.ArticlePost.objects.all().order_by('-create_time')
        cache.set('articles_all', articles, 30 * 60)
    # 文章分类列表缓存
    if column and column != 'None':
        if cache.has_key('articles_{}'.format(column)):
            articles = cache.get('articles_{}'.format(column))
        else:
            if column and column != 'None':
                articles = models.ArticlePost.objects.all().filter(column_id=column)
                cache.set('articles_{}'.format(column), articles, 30 * 60)
    # 文章标签列表缓存
    if tag and tag != 'None':
        if cache.has_key('articles_{}'.format(tag)):
            articles = cache.get('articles_{}'.format(tag))
        else:
            # 标签查询集
            if tag and tag != 'None':
                articles = models.ArticlePost.objects.all().filter(tags__name__in=[tag])
                cache.set('articles_{}'.format(tag), articles, 30 * 60)
    # 每页显示 1 篇文章
    paginator = Paginator(articles, 10)
    # 获取url中的页码
    page = request.GET.get('page')
    # 获取所有的文章分类
    if cache.has_key("classify"):
        classify = cache.get("classify")
    else:
        classify = models.ArticleColumn.objects.all()
        cache.set("classify", classify, 24 * 60 * 60)
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    # 需要传递给模板（templates）的对象
    context = {'articles': articles, 'order': order, 'tag': tag, 'column': column, 'classify': classify,
               'friend_link': friend_link, 'five_articles': five_articles, 'five_new_articles': five_new_articles,
               'search_tag': tag}
    # render函数：载入模板，并返回context对象
    return render(request, 'index/list.html', context=context)

# 博客文章详情页面
def article_detail(request, id):
    # 详细页面文章缓存(根据对应的id进行缓存，并设置5分钟缓存时间)
    if cache.has_key('detail_article_{}'.format(id)):
        article = cache.get('detail_article_{}'.format(id))
    else:
        # 获取详细文章
        article = models.ArticlePost.objects.get(id=id)
        cache.set("detail_article_{}".format(id), article, 10 * 60)
    # 获取所有的文章分类
    if cache.has_key("classify"):
        classify = cache.get("classify")
    else:
        # 获取所有的文章分类
        classify = models.ArticleColumn.objects.all()
        cache.set("classify", classify, 24 * 60 * 60)
    # 2019年11.11日添加(获取与此相关的访问量前五名的文章)，加缓存
    if cache.has_key('five_articles_{}'.format(id)):
        five_articles = cache.get('five_articles_{}'.format(id))
    else:
        five_articles = models.ArticlePost.objects.filter(column=article.column).order_by('-article_view')
        if five_articles.count() > 5:
            five_articles = five_articles[:5]
        else:
            five_articles = five_articles[:]
        cache.set('five_articles_{}'.format(id), five_articles, 24 * 60 * 60)
    # 获取用户已经访问的前五篇文章
    ip_address = get_ip(request)
    all_article_read = models.ArticleDetailView.objects.all().filter(ip_address=ip_address).exclude(article_id=id).order_by('-time_update')
    if all_article_read.count() > 5:
        all_article_read = all_article_read[0:5]
    else:
        all_article_read = all_article_read[:]
    # 取出文章评论
    comments = Comments.objects.filter(article=id)
    # 过滤出所有的id比当前文章小的文章
    pre_article = models.ArticlePost.objects.filter(id__lt=article.id).order_by('-id')
    # 过滤出id大的文章
    next_article = models.ArticlePost.objects.filter(id__gt=article.id).order_by('id')
    # 取出相邻前一篇文章
    if pre_article.count() > 0:
        pre_article = pre_article[0]
    else:
        pre_article = None
    # 取出相邻后一篇文章
    if next_article.count() > 0:
        next_article = next_article[0]
    else:
        next_article = None
    article.article_view += 1
    article.save(update_fields=['article_view'])
    # 引入评论表单
    comment_form = CommentForm()
    context = {'article': article,  'comments': comments, 'pre_article': pre_article,
               'next_article': next_article, 'five_articles': five_articles, 'classify': classify,
               'all_articles': all_article_read, 'comment_form': comment_form}
    return render(request, 'article/detail.html', context=context)

# 点赞数 +1
@csrf_exempt
def increase_likes(request, id):
    ip_address = get_ip(request)
    article = models.ArticlePost.objects.get(id=id)
    ip_exist = models.ArticleLikes.objects.filter(article_id=id).filter(ip_address=ip_address)
    if ip_exist:
        ret = {
            'like': article.like,
            'status': 'fail',
        }
        return JsonResponse(ret)
    else:
        ip_location = ip_location_baidu(ip_address)
        models.ArticleLikes.objects.create(article_id=id, ip_address=ip_address, ip_loaction=ip_location)
        article.like += 1
        article.save()
        ret = {
            'like': article.like,
            'status': 'success',
        }
        return JsonResponse(ret)

# 获取用户ip归属地
def ip_location_baidu(ip):
    response = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
    if response.json()['code'] == 0:
        data = response.json()['data']
        country = data['country']   # 国家
        # area = data['area']   # 区域
        region = data['region']  # 地区
        city = data['city']  # 城市
        isp = data['isp']  # 运营商
        ip_location = country+region+city+isp
    else:
        ip_location = '未查询到！'
    return ip_location

#  统计用户访问详情页面的次数
def visit_article(request, id):
    response = {
        'msg': "请求成功",
        'status': 'success',
    }
    ip_address = get_ip(request)
    ip_exist = models.ArticleDetailView.objects.filter(ip_address=ip_address).filter(article_id=id)
    if ip_exist:
        ip_exist = models.ArticleDetailView.objects.all().filter(article_id=id).get(ip_address=ip_address)
        ip_exist.visit_number += 1
        ip_exist.save()
    else:
        ip_location = ip_location_baidu(ip_address)
        models.ArticleDetailView.objects.create(article_id=id, ip_address=ip_address, ip_loaction=ip_location)
    return JsonResponse(response)

#  统计用户访问主页的次数
def visit_web(request):
    response = {
        'msg': "数据保存成功",
        'status': 'success',
    }
    if request.method == "POST" and request.POST:
        ip_address = get_ip(request)
        cur_url = request.POST.get("cur_url", None)
        if cur_url:
            ip_exist = models.SeeMyWebsite.objects.filter(ip_address=ip_address)
            if ip_exist:
                ip_exist = models.SeeMyWebsite.objects.get(ip_address=ip_address)
                ip_exist.visit_number += 1
                ip_exist.save()
            else:
                ip_location = ip_location_baidu(ip_address)
                models.SeeMyWebsite.objects.create(ip_address=ip_address, ip_loaction=ip_location)
        else:
            response['status'] = 'fail'
            response['msg'] = '数据保存失败'
    return JsonResponse(response)

def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            new_article.save()
            # 新增代码，保存 tags 的多对多关系
            article_post_form.save_m2m()

            return redirect("index:blog_list")
        else:
            return HttpResponse("表单提交的数据有误！")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'index/create.html', context)

# 网站页面错误时候
def page_not_found(request):
    return render(request, 'error/404.html')

def page_error(request):
    return render(request, 'error/404.html')