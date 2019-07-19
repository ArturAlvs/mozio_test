from rest_framework import routers
from .api_view import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet)

router.register(r'servicearea', ServiceAreaViewSet)
