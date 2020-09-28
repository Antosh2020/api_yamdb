from .models import Category, Genre, Title
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name', 'slug')
        model = Category
        
        
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name', 'slug')
        model = Genre
        

class TitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Title
        