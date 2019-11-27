from django.contrib.sitemaps import Sitemap

from .models import ArticlePost

class PostSitemap(Sitemap):
    # 当前条目修改的频率（可选参数）
    changefreq = 'daily'
    # 当前条目在网站中的权重系数（可选参数）
    priority = 0.9
    # 定义网站地图中的网址的协议（可选参数）
    protocol = 'https'
    # 必须定义的
    def items(self):
        return ArticlePost.objects.all()

    def lastmod(self, obj):
        return obj.create_time
