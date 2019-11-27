from django.contrib import admin
from .models import Development

# Register your models here.
class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ['story_title', 'story_line_photo', 'story_text', 'story_time', 'story_time_update']

admin.site.register(Development, DevelopmentAdmin)