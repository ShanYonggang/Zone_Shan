from django.urls import path
from . import views

app_name = 'friend_url'

urlpatterns = [
    path('', views.get_friend_link, name='link'),
    path('add_friend_link/', views.friend_url_add, name='add_link'),
]