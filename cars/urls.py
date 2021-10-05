from django.urls import path
from .views import ListCar, CarUpdateAPIView


urlpatterns = [
    path('cars/', ListCar.as_view()),
    path('cars/update/<int:id>', CarUpdateAPIView.as_view()),

]