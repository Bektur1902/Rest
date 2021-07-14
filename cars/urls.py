from django.urls import path
from .views import *

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/read/', CarListView.as_view()),
    path('car/update/<int:pk>', CarDetailView.as_view()),
]