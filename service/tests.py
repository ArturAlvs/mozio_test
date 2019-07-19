from django.test import TestCase

# Create your tests here.
from django.contrib.gis.geos import Polygon, GEOSGeometry, Point
from .models import *


import string
import random


# Test Velocity
import datetime
from django.utils.timezone import utc


class PointInPolygonTestCase(TestCase):

    """
    This is a class to test is Point is inside Polygon

    It create a Provider and 2 Polygons as database data


    """

    def setUp(self):

        # creatinf PROVIDER and SERVICE AREA to test if a Point is inside that Polygon
        provider = Provider.objects.create(name="TestUser_1", email="user1@email.com", phone_number="+5521", language="English", currency="USD")

        poly_one = Polygon( ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)) )
        ServiceArea.objects.create(provider=provider, name="City1", price=10.0, poly=poly_one)


        poly_two = Polygon( ((0.0, 0.0), (0.0, 5.0), (5.0, 5.0), (5.0, 0.0), (0.0, 0.0)) )
        ServiceArea.objects.create(provider=provider, name="City2", price=10.0, poly=poly_two)


    def test_point_inside_polygon(self):
        """

        The test function creates a Point inside the first Service Area coordinates
            than the function checks if the point is indeed inside the Service Area

        """

        pnt = GEOSGeometry('POINT(%s %s)' % ("30.0", "10.0"))

        data = ServiceArea.objects.all()

        for service_area in data:

            if service_area.name == "City1":
                self.assertEqual( service_area.poly.contains(pnt), True)
            else:
                self.assertEqual( service_area.poly.contains(pnt), False)



class VelocityTestCase(TestCase):

     """
    This is a class to test is Velocity of search

    It creates:
        100 Providers and 100 Service Area for each provider
        1 Provider with 1 Service Area tha include the Point to be created


    """

    def setUp(self):

        # looping to create data fo testing
        for x in range(0,100):

            name = ""
            email = ""
            phone_number = ""
            language = ""

            # looping to create combinations for PROVIDER data
            for letra in range(0,10):
                name = name + random.choice(string.ascii_letters)
                email = email + random.choice(string.ascii_letters)
                phone_number = phone_number + random.choice(string.ascii_letters)
                language = language + random.choice(string.ascii_letters)

            provider = Provider.objects.create(name=name, email=email, phone_number=phone_number, language=language, currency="USD")

            # looping to create combinations for SERVICE AREA data
            for y in range(0,100):
                number = random.randint(0,5000)

                poly = Polygon( ((0.0, 0.0), (0.0, number), (number, number), (number, 0.0), (0.0, 0.0)) )
                city_name = "City" + str(x)
                ServiceArea.objects.create(provider=provider, name=city_name, price=10.0, poly=poly)



        # PROVIDER and SERVICE AREA that contain the point
        # creating to test how fast it can retrieve the data
        provider = Provider.objects.create(name="TestUser_1", email="user1@email.com", phone_number="+5521", language="English", currency="USD")
        poly = Polygon( ((5000.0, 5000.0), (5000.0, 6000.0), (6000.0, 6000.0), (6000.0, 5000.0), (5000.0, 5000.0)) )
        ServiceArea.objects.create(provider=provider, name="MyCity", price=10.0, poly=poly)


    def test_point_inside_polygon_all_search(self):

        """
        This function create a Point inside a Provider's Service Area
            than the function perform query to retrieve all Service Areas to check if point is inside

        DATA FROM MY MACHINE TEST

        # TIME FOR ALL SEARCH::::::
        # 0.354584 seconds
        # TIME FOR ALL SEARCH::::::

        """

        pnt = GEOSGeometry('POINT(%s %s)' % ("5001.0", "5001.0"))

        before = datetime.datetime.utcnow().replace(tzinfo=utc)

        data = ServiceArea.objects.all()

        for service_area in data:

            if service_area.poly.contains(pnt):
                pass

        after = datetime.datetime.utcnow().replace(tzinfo=utc)

        print("TIME FOR ALL SEARCH::::::")
        print( (after - before).total_seconds() )
        print("TIME FOR ALL SEARCH::::::")

        print(data)

    def test_point_inside_polygon_filter_search(self):

        """
        This function create a Point inside a Provider's Service Area
            than the function perform query to retrieve only Service Areas with the Point inside

        DATA FROM MY MACHINE TEST

        # TIME FOR ALL SEARCH::::::
        # 0.000635 seconds
        # TIME FOR ALL SEARCH::::::

        """

        pnt = GEOSGeometry('POINT(%s %s)' % ("5001.0", "5001.0"))

        before = datetime.datetime.utcnow().replace(tzinfo=utc)

        data = ServiceArea.objects.filter(poly__contains=pnt)

        after = datetime.datetime.utcnow().replace(tzinfo=utc)


        print("TIME FILTER SEARCH::::::")
        print( (after - before).total_seconds() )
        print("TIME FILTER SEARCH::::::")

        print(data)

