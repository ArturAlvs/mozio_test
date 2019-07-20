from django.db import models

from django.contrib.gis.db import models as geomodels
# Create your models here.

class Provider(models.Model):

    """
    This is a class is a Model to Provider information

    :type name: string
    :param name: the name of Provider

    :type email: EmailField
    :param email: the email of Provider

    :type phone_number: string
    :param phone_number: the phone number of Provider

    :type langague: string
    :param langague: the langague that Provider use

    :type currency: string
    :param currency: the currency that Provider use

    """

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

    """
    This is a class is a Model to Service Area information

    A Service Area is where the Provider provide their service


    :type provider: ForeignKey
    :param provider: the Provider of the Service Area

    :type name: string
    :param name: the name of Service Area

    :type price: DecimalField
    :param price: the price of Service Area

    :type poly: PolygonField
    :param poly: the Polygon representing the area

    """

    provider = geomodels.ForeignKey(Provider, on_delete=models.CASCADE)

    name = geomodels.CharField(max_length=50, help_text="service area name.")

    price = geomodels.DecimalField(max_digits=8, decimal_places=2)

    poly = geomodels.PolygonField()

    # so I could see on admin page
    def __str__(self):
        return self.name