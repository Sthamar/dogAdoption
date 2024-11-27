from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.text import slugify
# Create your models here.

class Dog(models.Model):
    SEX_TYPE = [('Male','Male'), ('Female','Female')]
    
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    breed = models.CharField(max_length=200)
    age = models.IntegerField()
    image = models.ImageField()
    sex  = models.CharField(max_length=200, null=False, choices=SEX_TYPE)
    slug = models.SlugField(null=True,blank=True, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Adopter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?\d{9,15}$', message="Enter a valid phone number.")])
    address = models.CharField(max_length=200)
    adopted_dogs = models.OneToOneField(Dog, on_delete=models.CASCADE,related_name='adopters', null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'