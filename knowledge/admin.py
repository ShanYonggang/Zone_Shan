from django.contrib import admin
from .models import MyKnowledgeUrl, MyBookShare, MySoftware

# Register your models here.
class MyKnowledgeUrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'search_url')
    list_filter = ('name',)
    search_fields = ('search_url', 'name')
    raw_id_fields = ('name',)
    date_hierarchy = 'create_time'
    ordering = ['create_time', 'name']
admin.site.register(MyKnowledgeUrl, MyKnowledgeUrlAdmin)

class MyBookShareAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'download')
    list_filter = ('title',)
    search_fields = ('download', 'title')
    raw_id_fields = ('title',)
    date_hierarchy = 'create_time'
    ordering = ['create_time', 'title']
admin.site.register(MyBookShare, MyBookShareAdmin)

class MySoftwareAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'download')
    list_filter = ('title',)
    search_fields = ('download', 'title')
    raw_id_fields = ('title',)
    date_hierarchy = 'create_time'
    ordering = ['create_time', 'title']
admin.site.register(MySoftware, MySoftwareAdmin)