from .views import *
from django.urls import path

urlpatterns = [
    path('',home,name='base_view_basepage'),
]
