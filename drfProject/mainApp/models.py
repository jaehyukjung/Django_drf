from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class Coffee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50) 
    cups = models.IntegerField(null=True)

