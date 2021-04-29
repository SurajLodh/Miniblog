from django.db import models

# Create your models here.

class Blogs(models.Model):
    title =models.TextField(max_length=20)
    dis = models.TextField()