from django.urls import path
from . import views
from .views import store_data_into_database

urlpatterns = [
    path('transform_csv/', views.store_data_into_database)
]