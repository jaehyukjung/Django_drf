from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail, CoffeeList, CoffeeDetail

urlpatterns = [
    path('review/', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('coffee/', CoffeeList.as_view()),
    path('coffee/<int:pk>/', CoffeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)