from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published_year = models.IntegerField()

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)