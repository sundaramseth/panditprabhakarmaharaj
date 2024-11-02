from django.contrib.sitemaps import Sitemap
from services.models import Typesofpuja
from django.urls import reverse

class TypesofpujaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Typesofpuja.objects.filter()

    def lastmod(self, obj):
        return obj.updated_at

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
