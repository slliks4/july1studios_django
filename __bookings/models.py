from django.db import models

class Category(models.Model):
    category_name= models.CharField(max_length=200, verbose_name='event_category')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return f'{self.category_name}'
    

class Booking(models.Model):
    event_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    date= models.DateField(null=True, blank=True)
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    email=models.EmailField()
    tel=models.CharField(max_length=100)
    event_location=models.CharField(max_length=200)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    description=models.TextField()
    booking_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.event_category} || {self.first_name} {self.last_name} || {self.booking_date}'