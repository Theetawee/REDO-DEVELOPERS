from django.db import models

# Create your models here.


class Testimony(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="testimonies/")
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.name
