from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户登出
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.user_register_no_form, name='register'),
    # 用户更新(更新除了头像的信息)
    path('update/', views.user_update, name='update'),
    # 用户修改个人头像信息 (暂时保存)
    path('user_info/', views.user_info, name='user_info'),
]