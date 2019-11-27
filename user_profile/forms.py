from django import forms
from user_profile.models import UserProfile
import re

def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(label='确认密码',required=True,widget=forms.PasswordInput)
    
    class Meta:
        model = UserProfile
        fields = ['username','password','email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            filter_result = UserProfile.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                value = "username_exist"
                raise forms.ValidationError(value)
        else:
            value = "Please Input an Username."
            raise forms.ValidationError(value)
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = UserProfile.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                value = "Your email already exists."
                raise forms.ValidationError(value)
        else:
            value = "Please enter a valid email."
            raise forms.ValidationError(value)
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1)<6:
            value = "请至少输入六位密码！"
            raise forms.ValidationError(value)
        elif len(password1)>15:
            value = "您的密码太长，请输入15位以内的密码！"
            raise forms.ValidationError(value)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            value = "Password mismatch. Please enter again."
            raise forms.ValidationError(value)
        return password2

class LoginForm(forms.Form):
    
    username = forms.CharField(label='用户名',required=True)
    password = forms.CharField(label='密码',required=True,widget=forms.PasswordInput)

    # class Meta:
    #     model = UserProfile
    #     fields = ['username','password','email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if email_check(username):
            filter_result = UserProfile.objects.filter(email__exact=username)
            if not filter_result:
                value = "This Email Does Not Exist!"
                raise forms.ValidationError(value)
        else:
            filter_result = UserProfile.objects.filter(username__exact=username)
            print(filter_result)
            if not filter_result:
                value = 'This UserName Does Not Exist!'
                raise forms.ValidationError(value)
        return username
            