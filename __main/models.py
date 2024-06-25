from django.db import models

class First_slide(models.Model):
    pic=models.ImageField(null=True, blank=True, upload_to='img')
    title=models.CharField(max_length=200)
    date=models.DateField()

    def __str__(self) -> str:
        return f'{self.title} || {self.date}'
    
class Gallery_slide(models.Model):
    pic=models.ImageField(null=True, blank=True, upload_to='img')
    date=models.DateField()

    class Meta:
        ordering=['-date',]

    def __str__(self) -> str:
        return f'{self.date}'
    
class Event_slide(models.Model):
    pic=models.ImageField(null=True, blank=True, upload_to='img')
    date=models.DateField()

    class Meta:
        verbose_name_plural='Recent_events'
        ordering=['-date',]

    def __str__(self) -> str:
        return f'{self.date}'
    
class Our_service(models.Model):
    pic=models.ImageField(null=True, blank=True, upload_to='img')

    def __str__(self) -> str:
        return f'{self.pic}'

class Comments(models.Model):
    comment=models.TextField()
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Comments'

    def __str__(self) -> str:
        return f'{self.name} || {self.email}'