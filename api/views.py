from rest_framework import viewsets, mixins, filters
from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
#from api.permissions import


class CategoryViewSet(GenericViewSet, mixins.CreateModelMixin,
                      mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#   permission_classes = [IsAuthenticatedOrReadOnly, IsOwner, IsAdmin]
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination
    search_fields = ['=name']


class GenreViewSet(GenericViewSet, mixins.CreateModelMixin,
                   mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly, IsOwner, IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly, IsOwner, IsAdmin]