from django.db import models

from django.contrib.gis.db import models as geomodels
# Create your models here.

class Provider(models.Model):

    name = models.CharField(max_length=50, help_text="provider name.")
    email = models.EmailField(max_length=50, help_text="provider email.")

    # could use django-phonenumber-field library
    phone_number = models.CharField(max_length=16, help_text="provider phone number.")

    # could use django-language-field library
    language = models.CharField(max_length=25, help_text="provider language.")

    # could use django-money library
    currency = models.CharField(max_length=50, help_text="currency used by provider.")


    # so I could see on admin page
    def __str__(self):
        return self.name



class ServiceArea(geomodels.Model):
    provider = geomodels.ForeignKey(Provider, on_delete=models.CASCADE)

    name = geomodels.CharField(max_length=50, help_text="service area name.")

    price = geomodels.DecimalField(max_digits=8, decimal_places=2)

    poly = geomodels.PolygonField()


    # so I could see on admin page
    def __str__(self):
        return self.name