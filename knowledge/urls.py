from django.urls import path
from . import views

app_name = 'knowledge'

urlpatterns = [
    # 知识页
    path('', views.get_knowledge, name='get_knowledge'),
]