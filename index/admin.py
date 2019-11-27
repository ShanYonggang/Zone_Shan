from django.contrib import admin
from .models import ArticlePost
from .models import ArticleColumn,ArticleLikes,SeeMyWebsite,ArticleDetailView

# Register your models here.
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'update_time', 'author','column')
    list_filter = ('update_time','author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'update_time'
    ordering = ['update_time','author']

admin.site.register(ArticlePost,ArticlePostAdmin)

admin.site.site_header = '大圣的个人网站'
admin.site.site_title = '大圣的个人网站后台管理系统'

# 注册文章栏目
admin.site.register(ArticleColumn)

# 注册用户点赞信息
class ArticleLikesAdmin(admin.ModelAdmin):
    list_display = ('id','ip_address','article', 'ip_loaction','time_update')
    list_filter = ('time_update','ip_address')
    search_fields = ('ip_loaction', 'time_create')
    date_hierarchy = 'time_update'
    ordering = ['time_update','ip_address']
admin.site.register(ArticleLikes,ArticleLikesAdmin)

# 注册主页访问信息
class SeeMyWebsiteAdmin(admin.ModelAdmin):
    list_display = ('id','ip_address','visit_number', 'ip_loaction','time_update')
    list_filter = ('time_update','ip_address')
    search_fields = ('ip_loaction', 'time_create')
    date_hierarchy = 'time_update'
    ordering = ['time_update','ip_address']
admin.site.register(SeeMyWebsite,SeeMyWebsiteAdmin)

# 注册文章访问信息
class ArticleDetailViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_address', 'article', 'ip_loaction', 'time_update','visit_number')
    list_filter = ('time_update', 'ip_address')
    search_fields = ('ip_loaction', 'time_create')
    date_hierarchy = 'time_update'
    ordering = ['time_update', 'ip_address']
admin.site.register(ArticleDetailView, ArticleDetailViewAdmin)