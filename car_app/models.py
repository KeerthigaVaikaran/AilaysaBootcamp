from django.db import models


""" Model for Manufacturer Details """
class Manufacturer(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    founded=models.IntegerField()
    def __str__(self):
        return self.name
    
""" Model for Car Feature Details """
    
class CarFeature(models.Model):
    feature_name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.feature_name
    
    
""" Model for Car Details """
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    carfeature=models.ManyToManyField(CarFeature, related_name='carsfeature')
    
    def __str__(self):
        return self.model_name 
""" Model for Reviews """
  
class CarReview(models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_review')
    review=models.TextField()
    def __str__(self):
        return "Review for" + self.car.model_name 
