from django.urls import path

from . import views

urlpatterns = [
    path('rsmi', views.rsmi, name='reports-rsmi'),
    path('ledger', views.ledger, name='reports-ledger'),
]
