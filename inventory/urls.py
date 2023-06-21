from django.urls import path

from . import views

urlpatterns = [
        path('po', views.po, name='inventory-po'),
        path('ris', views.ris, name='inventory-ris'),
        path('transaction', views.transaction, name='inventory-transaction'),
        path('summary', views.summary, name='inventory-summary'),
]
