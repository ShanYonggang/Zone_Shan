from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http import JsonResponse
from django.urls import reverse
from . import forms
from user_profile.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
import re
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password  # 密码加密
from .models import UserProfile
import json


# Create your views here.

# 用户注册
# 验证邮箱
def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        print(register_form)
        emaild = request.POST.get('email')
        print(emaild)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            print(username)
            if username == 'username_1':
                return HttpResponse('{"status": "fail", "msg": "用户名已存在!"}')
            elif username == 'username_2':
                return HttpResponse('{"status": "fail", "msg": "请输入一个用户名!"}')
            email = register_form.cleaned_data['email']
            print(email)
            if email == 'email_1':
                return HttpResponse('{"status": "fail", "msg": "邮箱已经存在!"}')
            elif email == 'email_2':
                return HttpResponse('{"status": "fail", "msg": "请输入一个邮箱名!"}')
            password1 = register_form.cleaned_data['password']
            print(password1)
            password2 = register_form.cleaned_data['password2']
            print(password2)
            if password1 == 'password_1':
                return HttpResponse('{"status": "fail", "msg": "请至少输入六位密码！"}')
            elif password1 == 'password_2':
                return HttpResponse('{"status": "fail", "msg": "您的密码太长，请输入15位以内的密码！"}')
            UserProfile.objects.create(username=username, password=password1, email=email)
            print('Save Success!')
            return HttpResponse('{"status": "success"}')
        else:
            print('Save Fail!')
            return HttpResponse('{"status": "fail", "msg": "您输入的密码有误！"}')
    else:
        form = forms.RegisterForm()
    return render(request, 'users/registration.html', {'form': form})


# 用户登录
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        username_or_not = UserProfile.objects.filter(username=username)
        if username_or_not:
            username_or_not = UserProfile.objects.get(username=username)
            if not check_password(pwd, username_or_not.password):
                return HttpResponse('{"status":"fail","msg":"您输入的密码有误！"}')
        else:
            return HttpResponse('{"status":"fail","msg":"用户名不存在！"}')
        user = auth.authenticate(username=username, password=pwd)
        if user is not None and user.is_active:
            # 登录成功
            auth.login(request, user)
            return HttpResponse('{"status":"success"}')


# 用户退出
def user_logout(request):
    logout(request)
    return redirect("index:blog_list")


# 用户注册(没有用表单验证)
@csrf_exempt
def user_register_no_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        username = request.POST.get("username")
        # 验证username
        filter_result = UserProfile.objects.filter(username=username)
        if username:
            if len(filter_result) > 0:
                #  表示用户已经存在
                return HttpResponse('{"status":"fail","msg":"该用户名已存在"}')
        else:
            # 表示用户未输入用户名
            return HttpResponse('{"status":"fail","msg":"请输入一个用户名"}')
        # 验证email
        filter_result = UserProfile.objects.filter(email=email)
        if email_check(email):
            if len(filter_result) > 0:
                #  表示该邮箱已经注册
                return HttpResponse('{"status":"fail","msg":"该邮箱已经注册"}')
        else:
            # 表示用户未输入邮箱
            return HttpResponse('{"status":"fail","msg":"请输入一个正确的邮箱"}')
        # 验证密码
        if len(password1) < 6:
            return HttpResponse('{"status":"fail","msg":"请输入一个至少6位数的密码"}')  # 表示密码少于6位
        elif len(password1) > 15:
            return HttpResponse('{"status":"fail","msg":"请输入一个最多15位数的密码"}')  # 表示密码多于15位
        # 验证密码是否一致
        if password1 and password2 and password1 != password2:
            return HttpResponse('{"status":"fail","msg":"请查看两次密码是否输入一致"}')
        # 验证完成，保存数据
        password1 = make_password(password1)
        UserProfile.objects.create(username=username, password=password1, email=email)
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return HttpResponse('{"status":"success"}')


@csrf_exempt
def user_info(request):
    '''用户头像上传更新'''
    if request.method == "POST":
        # image_file = request.FILES.get('image')
        image_file = request.POST['image']
        if image_file:
            _t = UserProfile.objects.get(id=request.user.id)
            _t.user_photo = image_file
            _t.save()
            to_json_response = {
                'result': '头像上传成功'
            }
            return HttpResponse(json.dumps(to_json_response), content_type='application/json')
        else:
            to_json_response = {
                'result': '头像上传失败'
            }
            return HttpResponse(json.dumps(to_json_response), content_type='application/json')
    return render(request, 'userprofile/userinfo.html')


#  用户信息更新
@csrf_exempt
def user_update(request):
    # return HttpResponse("进入用户编辑页面")
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        your_url = request.POST.get('user_url')
        email = request.POST.get('email')
        wechat = request.POST.get('wechat')
        qq = request.POST.get('qq')
        image = request.FILES.get('images')
        if request.user:
            user_info = UserProfile.objects.get(username=request.user)
            if nickname:
                user_info.nickname = nickname
            if phone:
                user_info.phone = phone
            if your_url:
                user_info.your_url = your_url
            if email:
                user_info.email = email
            if qq:
                user_info.QQ_num = qq
            if wechat:
                user_info.wechat = qq
            if image:
                user_info.avatar = image
            user_info.save()
            return redirect('/userprofile/update/')
        return redirect('/userprofile/update/')
    return render(request, 'userprofile/userinfo.html')