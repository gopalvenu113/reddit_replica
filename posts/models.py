from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

