from django.db import models

# Create your models here.
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact)
    def __str__(self):
        return self.name
