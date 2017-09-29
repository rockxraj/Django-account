from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    branch = models.CharField(max_length=200, null=False)

    
