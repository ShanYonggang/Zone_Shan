from django import forms
from django.forms.widgets import TextInput
from .models import FriendLink
import requests

class FriendsURLForm(forms.ModelForm):

    def clean_friend_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        friend_url = self.cleaned_data.get('friend_url').strip()
        try:
            response = requests.get(friend_url, headers=headers, timeout=5)
            print(response.status_code)
            if response.status_code == 200:
                print('提交成功！！')
                print(response.status_code)
                return friend_url
            else:
                value = "网站链接无法连接，请检查网站链接填写是否正确"
                raise forms.ValidationError(value)
        except Exception as e:
            raise forms.ValidationError("网站链接无法连接，请检查网站链接填写是否正确")

    class Meta:
        model = FriendLink
        fields = ['name', 'your_email', 'website_name', 'friend_url', 'url_image']
        widgets = {
            'name': TextInput(attrs={'placeholder': '怎么称呼您'}),
            'your_email': TextInput(attrs={'placeholder': '邮箱与上次一致时可以修改其他信息'}),
            'website_name': TextInput(attrs={'placeholder': '友情链接显示名称，认真填写哦'}),
            'friend_url': TextInput(attrs={'placeholder': '请在输入前确保自己的网站可以访问'}),
        }