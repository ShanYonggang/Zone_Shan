from django.contrib import admin
from .models import Comments
# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'body', 'created')
    list_filter = ('user','created')
    search_fields = ('article', 'user', 'body', 'created')
    date_hierarchy = 'created'
    ordering = ['created','user']

admin.site.register(Comments, CommentsAdmin)

admin.site.site_header = '大圣的个人网站'
admin.site.site_title = '大圣的个人网站后台管理系统'