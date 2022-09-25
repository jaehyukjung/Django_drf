from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import ReviewSerializer,CoffeeSerializer
from .models import Coffee, Review

from django.template import loader
import my_stt


# Create your views here.


class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 성공한 경우에는 200포트
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 실패한 경우에는 400포트

class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk = pk)
        except Review.DoesNotExist:
            raise Http404
    
    def get(self, request,pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CoffeeList(APIView):
    def get(self, request):
        reviews = Coffee.objects.all()
        serializer = CoffeeSerializer(reviews, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoffeeSerializer(
            data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 성공한 경우에는 200포트
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 실패한 경우에는 400포트

class CoffeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Coffee.objects.get(pk = pk)
        except Coffee.DoesNotExist:
            raise Http404
    
    def get(self, request,pk, format=None):
        review = self.get_object(pk)
        serializer = CoffeeSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = CoffeeSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderList(APIView):
    def get(self, request):
        lst = my_stt.my_fun()
        
        reviews = Coffee.objects.filter(name__in= lst)
        serializer = CoffeeSerializer(reviews, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoffeeSerializer(
            data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 성공한 경우에는 200포트
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 실패한 경우에는 400포트

class OrderDetail(APIView):
    def get_object(self, pk):
        try:
            return Coffee.objects.get(pk = pk)
        except Coffee.DoesNotExist:
            raise Http404
    
    def get(self, request,pk, format=None):
        review = self.get_object(pk)
        serializer = CoffeeSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = CoffeeSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
