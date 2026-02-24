from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)