from django.db import models

class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Contact_form'

    def __str__(self) -> str:
        return f'{self.first_name}|| {self.email}|| {self.date}'
    

class News_letter(models.Model):
    email=models.EmailField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.email}|| {self.date}|| {self.time}'