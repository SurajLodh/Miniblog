from django.db import models

# Create your models here.

class Blogs(models.Model):
    title =models.TextField(max_length=50)
    dis = models.TextField()