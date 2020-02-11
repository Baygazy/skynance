from django.urls import path

from .views import *

urlpatterns = [
    # nav bar
    path('', HomeView.as_view(), name='home'),

    path('faq/', FaqView.as_view(), name='faq'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # sidebar menu
    path('investment/', InvestmentView.as_view(), name='investment'),
    path('investments/', InvestmentsView.as_view(), name='investments'),
    path('refill/', RefillView.as_view(), name='refill'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('profile-settings/', ProfileSettingsView.as_view(), name='profile-settings'),
    # path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('chat/', ChatView.as_view(), name='chat'),

    # footer
    # path('login/', LoginView.as_view(), name='login'),
]