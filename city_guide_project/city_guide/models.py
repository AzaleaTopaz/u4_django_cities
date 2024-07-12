from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    entrance_fee = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.CharField(max_length = 500)

    def __str__(self):
        return f'{self.reviewer_name} - {self.rating}'
