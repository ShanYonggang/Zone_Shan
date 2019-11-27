from django.contrib.sitemaps import Sitemap
# from .models import ArticlePost

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return ArticlePost.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.create_time
