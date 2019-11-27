from django.contrib import admin
from .models import UserProfile

# Register your models here.
# 用户注册信息
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname',  'email', 'your_url', 'wechat', 'QQ_num', 'c_time', 'last_login')
    list_filter = ('username', 'last_login')
    search_fields = ('username', 'last_login')
    date_hierarchy = 'last_login'
    ordering = ['username', 'last_login']
admin.site.register(UserProfile, UserProfileAdmin)