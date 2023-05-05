from django.urls import path

from . import views

urlpatterns = [
        path('user', views.user, name='user-list'),
        path('adduser', views.adduser, name='add-user'),
        path('updateuser', views.updateuser, name='update-user'),

        path('responsibilitycenter', views.responsibilitycenter, name='responsibility-center'),
        path('addresponsibilitycenter', views.addresponsibilitycenter, name='add-responsibility-center'),
        path('updateresponsibilitycenter', views.updateresponsibilitycenter, name='update-responsibility-center'),
        
        path('fundsource', views.fundsource, name='fund-source'),
        path('addfundsource', views.addfundsource, name='add-fund-source'),
        path('updatefundsource', views.updatefundsource, name='update-fund-source'),

        path('uacs', views.uacs, name='uacs'),
        path('adduacs', views.adduacs, name='add-uacs'),
        path('updateuacs', views.updateuacs, name='update-uacs'),

        path('units', views.units, name='units'),
        path('addunits', views.addunits, name='add-units'),
        path('updateunits', views.updateunits, name='update-units'),
        path('unitdetails', views.unitdetails, name='unit-details'),

]
