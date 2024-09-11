from django.urls import path
from . import views

urlpatterns = [
    path('activation/', views.account_activation_view, name='account_activation'),
    path('activation/step2/', views.account_activation_step2, name='account_activation_step2'),
    path('activation/success/', views.account_activation_success, name='account_activation_success'),
]
