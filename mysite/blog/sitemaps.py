# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/31 21:47'

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish