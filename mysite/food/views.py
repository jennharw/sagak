# Create your views here.
from rest_framework import viewsets

from .models import Food
from .serializers import FoodSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodSearchViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        food_name = self.request.query_params.get('food_name', None)
        research_year = self.request.query_params.get('research_year', None)
        maker_name = self.request.query_params.get('maker_name', None)
        food_code = self.request.query_params.get('food_code', None)

        if food_name:
            queryset = queryset.filter(food_name__icontains=food_name)
        if research_year:
            queryset = queryset.filter(research_year=research_year)
        if maker_name:
            queryset = queryset.filter(maker_name__icontains=maker_name)
        if food_code:
            queryset = queryset.filter(food_cd=food_code)

        return queryset