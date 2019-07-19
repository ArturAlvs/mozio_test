from django.conf.urls import url, include

from .api import *

from .views import *

urlpatterns = [
    url(r'^api/', include(router.urls)),

    # can login in ADMIN page, bu I will leave it here if someday is needed
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # capturing lng/lat to match Point args position
    # should change to (?P<lat>-?\d+\.\d+)/(?P<lng>-?\d+\.\d+) IF have to match the test text (lat/lng)
    url(r'^query/(?P<lng>-?\d+\.\d+)/(?P<lat>-?\d+\.\d+)', Index.as_view()),

]