from django.urls import path

from .views import *

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]