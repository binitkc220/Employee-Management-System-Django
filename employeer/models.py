from django.db import models

class employees(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()