from django.contrib import admin
from .models import FriendLink
# Register your models here.

class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'friend_url', 'website_name', 'your_email','submit_time')
    list_filter = ('website_name','friend_url')
    search_fields = ('friend_url', 'website_name', 'your_email')
    date_hierarchy = 'submit_time'
    ordering = ['submit_time','name']

admin.site.register(FriendLink, FriendLinkAdmin)

admin.site.site_header = '大圣的个人网站'
admin.site.site_title = '大圣的个人网站后台管理系统'