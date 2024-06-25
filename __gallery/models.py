from django.db import models

class Category(models.Model):
    category_name= models.CharField(max_length=200, verbose_name='event_category')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return f'{self.category_name}'
    
class Gallery_page(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='gallery_page')
    pic=models.ImageField(null=True, blank=True, upload_to='img')
    date=models.DateField()

    class Meta:
        ordering=['-date',]

    def __str__(self) -> str:
        return f'{self.category} || {self.date}'