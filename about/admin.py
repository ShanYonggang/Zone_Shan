from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SkillType, AboutWebSkill, About_models

# Register your models here.
class AboutWebSkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'introduce_text', 'introduce_image', 'skill', 'skill_type', 'skill_open_time', 'skill_status']

admin.site.register(AboutWebSkill, AboutWebSkillAdmin)
admin.site.register(SkillType)

admin.site.site_header = '大圣的个人网站'
admin.site.site_title = '大圣的个人网站后台管理系统'

class About_modelsAdmin(admin.ModelAdmin):
    list_display = ('introduce', 'time_create', 'body')
    list_filter = ('introduce',)
    search_fields = ('introduce', 'body')
    raw_id_fields = ('introduce',)
    date_hierarchy = 'time_create'
    ordering = ['time_create', 'introduce']
admin.site.register(About_models, About_modelsAdmin)