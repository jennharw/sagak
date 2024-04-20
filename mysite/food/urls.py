from django.urls import include, path
from rest_framework import routers

from .views import FoodViewSet, FoodSearchViewSet

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet, 'food')
router.register(r'food-search', FoodSearchViewSet, 'search')

urlpatterns = [
    path('', include(router.urls)),
]
