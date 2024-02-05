from django.db import models
from django.urls import reverse

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    material = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})

class Purchase(models.Model):
    date = models.DateField('purchase date')
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.shoe.name} purchased on {self.date}"
    
    class Meta:
        ordering = ['-date']
