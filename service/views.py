from django.contrib.gis.db.models.functions import *

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import *

from django.contrib.gis.geos import GEOSGeometry, Point

import json


class Index(View):

    """
    This is a class to return a list of Polygons with a Point inside

    The Point is provided over GET with 2 arguments

    URL example:
    http://localhost:8000/query/-43.246307373046875/-22.80150330466968

    The first coordinate is longitude
    The first coordinate is latitude

    """


    def get(self, request, lat, lng):

        """
        This function receive two arguments and query the database for Polygons with the Point inside
        This method - filter - was faster than querying all the data and checking if the Point is inside. See test.py

        Than return an Json structure

        """

        # creating point with arguments
        pnt = GEOSGeometry('POINT(%s %s)' % (lng, lat))

        # retrieve only polygons with point inside
        query_data = ServiceArea.objects.filter(poly__contains=pnt)

        # list to store data
        list_with_data = []

        # looping to select which data to return
        for service_area in query_data:

            polygon_found = {}

            polygon_found["polygon_name"] = service_area.name
            polygon_found["polygon_price"] = float(service_area.price)
            polygon_found["provider_name"] = service_area.provider.name

            list_with_data.append( polygon_found )

        returned_data = {}
        returned_data["polygons_with_point"] = list_with_data

        return HttpResponse(json.dumps(returned_data))