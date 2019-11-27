"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from index.views import roots, page_not_found, page_error
# 消息通知
import notifications.urls
# 网站地图
from django.contrib.sitemaps.views import sitemap
from index.sitemaps import PostSitemap
sitemaps = {
    'posts': PostSitemap,
}
# 定义错误跳转页面

handler404 = page_not_found
handler500 = page_error

urlpatterns = [
    path('my_web/', admin.site.urls),
    #  淘宝客验证文件
    path('jd_root.txt', roots),
    # 个人主页
    path('', include('index.urls', namespace='index')),
    # 用户个人信息
    path('userprofile/', include('user_profile.urls',namespace='user_profile')),
    # 评论
    path('comments/', include('comments.urls', namespace='comments')),
    # 评论
    path('about/', include('about.urls', namespace='about')),
    # 网站发展历程
    path('development/', include('development.urls', namespace='development')),
    # 友情链接
    path('friend_link/', include('friend_link.urls', namespace='friend_link')),
    # 资料文献模块
    path('knowledge/', include('knowledge.urls', namespace='knowledge')),
    # 全文搜索
    re_path(r'^search/', include('haystack.urls')),
    # 文件上传
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 第三方登录
    re_path(r'^accounts/', include('allauth.urls')),
    # 消息通知
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # 自定义消息模块
    path('notice/', include('notice.urls', namespace='notice')),
    #django-allauth用户自定义信息扩展
    # re_path(r'^accounts/', include('user_profile.urls', namespace='accounts')),
    # 网站地图
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

