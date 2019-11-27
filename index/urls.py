from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    # 所有文章列表
    path('', views.blog_list, name='blog_list'),
    # 文章详细页面
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    # 文章点赞功能
    path('increase-likes/<int:id>/', views.increase_likes, name='increase_likes'),
    # 主页ip访问量统计
    path('visit_web/', views.visit_web, name='visit_web'),
    # 详情页面访问统计
    path('visit_article/<int:id>/', views.visit_article, name='visit_article'),
]