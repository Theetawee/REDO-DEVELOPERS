from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CompanyRole(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    position = models.ManyToManyField(CompanyRole)
    profile_image = models.ImageField(
        upload_to="company_profiles/", blank=True, null=True
    )
    slug = models.SlugField(blank=True, null=True, max_length=255)
    template_name = models.CharField(max_length=255, default="default")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return f"{settings.STATIC_URL}/images/default.webp"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"slug": self.slug})


class Testimony(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonies/", blank=True, null=True)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=255, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class IPGeolocation(models.Model):
    ip = models.CharField(max_length=45)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timezone = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "IP Geolocation"
        verbose_name_plural = "IP Geolocations"


@receiver(post_save, sender=CompanyProfile)
def create_slug(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
