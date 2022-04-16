from rest_framework import viewsets

from task.models import Category, Subcategory, Advertisement
from task.serializers import CategorySerializer, SubcategorySerializer, AdvertisementSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.oblects.all()
    serializer_class = SubcategorySerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
