from django.contrib.sitemaps import Sitemap
from.models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    # receives each object from items and returns the time it was last modified
    def lastmod(self, obj):
        return obj.publish
