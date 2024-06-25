from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slug_generator

class News(models.Model):
    pic=models.ImageField(null=True, blank=True, upload_to='img')
    title= models.CharField(max_length=200) 
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    slug=models.SlugField(blank=True)

    class Meta:
        verbose_name_plural='News'
        ordering=['-date',]

    def __str__(self) -> str:
        return f'{self.title} || {self.date}'

def slug_generator(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=News)