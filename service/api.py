from rest_framework import routers
from .api_view import *

# Routers navigate in API
router = routers.DefaultRouter()

router.register(r'provider', ProviderViewSet)

router.register(r'servicearea', ServiceAreaViewSet)
