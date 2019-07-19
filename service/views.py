from django.contrib.gis.db.models.functions import *

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import *


class Index(View):


    def get(self, request):

        pego = ServiceArea.objects.all()

        print("OPA")

        print( pego[0].poly.area )

        print("OPA")


        print( pego[0].poly.json )

        print("OPA")



        return render(
            request,
            'index.html',
            context={ 'obj': pego },
        )
