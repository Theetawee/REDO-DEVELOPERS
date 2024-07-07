from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from main.models import CompanyProfile


class ProfileSitemap(Sitemap):
    changefreq = "hourly"
    priority = 1.0

    def items(self):
        return CompanyProfile.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    changefreq = "daily"  # Adjust the changefreq and priority as needed.
    priority = 1.0

    def items(self):
        # Define a list of static URLs you want to include in the sitemap.
        return ["home", "about", "leadership", "carrers", "contact", "services"]

    def location(self, item):
        # Define the URLs for each item in the list.
        return reverse(item)
