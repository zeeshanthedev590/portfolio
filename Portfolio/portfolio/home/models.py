from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField()

class Projects(models.Model):
    title = models.CharField(max_length=300)    
    desc = models.TextField()