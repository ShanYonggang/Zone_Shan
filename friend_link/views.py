from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import FriendLink
from .forms import FriendsURLForm
from index.models import ArticleColumn
# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
# 引入缓存
from django.core.cache import cache

# @cache_page(10 * 60)
def get_friend_link(request):
    # 友情列表缓存
    if cache.has_key("friend_link"):
        friend_link = cache.get("friend_link")
    else:
        # 获取所有的文章分类
        friend_link = FriendLink.objects.all().order_by('-submit_time')
        cache.set("friend_link", friend_link, 24 * 60 * 60)
    # 文章分类缓存
    if cache.has_key("classify"):
        classify = cache.get("classify")
    else:
        # 获取所有的文章分类
        classify = ArticleColumn.objects.all()
        cache.set("classify", classify, 24 * 60 * 60)
    context = {'friend_link': friend_link, 'classify': classify}
    return render(request, 'friend_link/friend_link.html', context=context)

@csrf_exempt
def friend_url_add(request):
    # return HttpResponse('hkjsa')
    if request.method == 'POST':
        form = FriendsURLForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            friend_url = form.cleaned_data['friend_url']
            website_name = form.cleaned_data['website_name']
            your_email = form.cleaned_data['your_email']
            url_image = form.cleaned_data['url_image']
            friend_link = FriendLink.objects.filter(your_email=your_email)
            if friend_link:
                friend_link = FriendLink.objects.get(your_email=your_email)
                friend_link.name = name
                friend_link.friend_url = friend_url
                friend_link.website_name = website_name
                friend_link.your_email = your_email
                friend_link.url_image = url_image
                friend_link.save()
                if cache.has_key("friend_link"):
                    cache.delete("friend_link")
                return redirect('friend_link:link')
            else:
                FriendLink.objects.create(name=name, friend_url=friend_url, website_name=website_name,
                                          your_email=your_email, url_image=url_image)
                if cache.has_key("friend_link"):
                    cache.delete("friend_link")
                return redirect('friend_link:link')
        else:
            form = FriendsURLForm()
            classify = ArticleColumn.objects.all()
    else:
        form = FriendsURLForm()
        classify = ArticleColumn.objects.all()
    return render(request, 'friend_link/friend_link_insert.html', {'form': form, 'classify':classify})
