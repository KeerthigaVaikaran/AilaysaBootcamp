from django.contrib import admin
from .models import Car,CarFeature,CarReview,Manufacturer

# Register your models here.
admin.site.register(CarReview)
admin.site.register(Car)
admin.site.register(CarFeature)
admin.site.register(Manufacturer)


