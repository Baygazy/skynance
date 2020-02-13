from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', SignUpView.as_view(), name='registration'),
    path('profile/', SignUpView.as_view(), name='registration'),
]