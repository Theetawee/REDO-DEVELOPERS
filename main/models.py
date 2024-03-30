from django.db import models
from django.conf import settings
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

    def __str__(self):
        return self.name

    @property
    def image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return f"{settings.STATIC_URL}/images/default.webp"


class Testimony(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonies/", blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class TestimonyMsg(models.Model):
    LANGUAGES = settings.LANGUAGES
    testmony = models.ForeignKey(Testimony, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    msg = models.TextField()
    lang = models.CharField(max_length=255, choices=settings.LANGUAGES, default="en")


@receiver(post_save, sender=CompanyProfile)
def create_slug(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
