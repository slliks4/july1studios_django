from django.db import models

class Vacancy(models.Model):
    pic=models.ImageField(blank=True, null=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Vacancies'

    def __str__(self) -> str:
        return f'{self.title}  ||  {self.date} {self.time}'
    

class Jobs_available(models.Model):
    vacancy= models.CharField(max_length=200, verbose_name='vacancy')

    class Meta:
        verbose_name_plural='Jobs_available'

    def __str__(self) -> str:
        return f'{self.vacancy}'
    
class Application(models.Model):
    vacancy=models.ForeignKey( Jobs_available ,on_delete=models.CASCADE )
    email=models.EmailField()
    tel=models.CharField(max_length=200)
    document=models.FileField()
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    description=models.TextField()   
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.vacancy}  ||  {self.first_name} {self.last_name}  || {self.date} '