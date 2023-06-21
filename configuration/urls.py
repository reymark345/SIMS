from django.urls import path

from . import views

urlpatterns = [
    path('beginning_balances', views.beginning_balances, name='configuration-beginning-balances'),
]
