from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('registration/', SignUpView.as_view(), name='registration'),
]