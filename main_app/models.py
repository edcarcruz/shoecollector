from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    material = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name