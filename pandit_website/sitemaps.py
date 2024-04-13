from django.contrib.sitemaps import Sitemap
from services.models import Typesofpuja


class TypesofpujaSitemap(Sitemap):
    def items(self):
        return Typesofpuja.objects.all()

    def lastmod(self, obj):
        return obj.updated_at