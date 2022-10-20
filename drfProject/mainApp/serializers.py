from rest_framework import serializers
from .models import Coffee, Review, Member

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member 
        fields = '__all__'


