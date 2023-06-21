from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import (AuthUser, UserDetails, LibResponsibilityCenter, LibFundSource, LibUacs, LibUnits, LibItems)
import json 
from django.core import serializers
import datetime
from django.contrib.auth.hashers import make_password



def user(request):
    context = {
		'users' : AuthUser.objects.filter().exclude(id=1).order_by('first_name').select_related('userdetails')
	}
    return render(request, 'admin/users.html', context)


@csrf_exempt
def adduser(request):
    if request.method == 'POST':
        
        firstname = request.POST.get('firstname')
        middle_name_ = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        email_ = request.POST.get('username')
        roles = request.POST.get('roles')
        birth_date = request.POST.get('birthdate')
        address_ = request.POST.get('address')
        sex_ = request.POST.get('sex')
        position_ = request.POST.get('position')

        print("testing")
        print(password_)

        if AuthUser.objects.filter(username=username_):
            print("halasaroles")
            return JsonResponse({'data': 'error'})
        else:
            add_authuser = AuthUser(
                password = make_password(password_),is_superuser = roles ,username= username_, first_name = firstname, last_name = lastname, email = email_, date_joined = datetime.datetime.now())
            add_authuser.save()
            
            add_user_details = UserDetails(
                middle_name = middle_name_ ,birthdate= birth_date, sex = sex_, address = address_, position = position_, user_id = AuthUser.objects.last().id)
            add_user_details.save()

            return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updateuser(request):
    if request.method == 'POST':
      
        user_id_ = request.POST.get('user_id')
        firstname = request.POST.get('firstname')
        middle_name_ = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        email_ = request.POST.get('email')
        roles = request.POST.get('roles')
        birth_date = request.POST.get('birthdate')
        address_ = request.POST.get('address')
        sex_ = request.POST.get('sex')
        position_ = request.POST.get('position')
        status = request.POST.get('is_active')

        if AuthUser.objects.filter(username=username_).exclude(id=user_id_):
            return JsonResponse({'data': 'error'})
        
        else:
            AuthUser.objects.filter(id=user_id_).update(password = make_password(password_),is_superuser = roles,username=username_,first_name=firstname,last_name=lastname, email = email_, is_active = status)
            UserDetails.objects.filter(user_id=user_id_).update(middle_name=middle_name_,birthdate=birth_date,sex=sex_, address = address_, position = position_)
            return JsonResponse({'data': 'success'})
        

def responsibilitycenter(request):
    context = {
		'responsibility_center' : LibResponsibilityCenter.objects.filter().order_by('acronym')
	}
    return render(request, 'admin/responsibility_center.html', context)


        
@csrf_exempt
def addresponsibilitycenter(request):
    if request.method == 'POST':
        rc_code = request.POST.get('rc_code')
        rc_acronym = request.POST.get('rc_acronym')
        rc_description = request.POST.get('rc_description')
        status = request.POST.get('is_active')
        
        if LibResponsibilityCenter.objects.filter(code=rc_code):
            return JsonResponse({'data': 'error'})
        else:
            add = LibResponsibilityCenter(
                code= rc_code,acronym = rc_acronym, description = rc_description,is_active = status)
            add.save()
        return JsonResponse({'data': 'success'})
    
    
@csrf_exempt
def updateresponsibilitycenter(request):
    if request.method == 'POST':
        rc_id = request.POST.get('rc_id')
        rc_code = request.POST.get('rc_code')
        rc_acronym = request.POST.get('rc_acronym')
        rc_description = request.POST.get('rc_description')
        status = request.POST.get('is_active')
    
        if LibResponsibilityCenter.objects.filter(code=rc_code).exclude(id=rc_id):
            return JsonResponse({'data': 'error'})
        else:
            LibResponsibilityCenter.objects.filter(id=rc_id).update(code=rc_code,acronym =rc_acronym,description=rc_description,is_active=status)
            return JsonResponse({'data': 'success'})
        

        
@csrf_exempt
def responsibilitycenterdetails(request):
    rc_id = request.POST.get('responsibility_center_id')
    qs_list = list(
         (LibResponsibilityCenter.objects
             .filter(id=rc_id)
             .values('code','acronym','description','is_active')
         )
    )
    return JsonResponse({'data': qs_list})


def fundsource(request):
    context = {
		'fund_source' : LibFundSource.objects.filter().order_by('name')
	}
    return render(request, 'admin/fund_source.html', context)
  
     
@csrf_exempt
def addfundsource(request):
    if request.method == 'POST':
        fundsource = request.POST.get('fundsource')
        cluster_name = request.POST.get('cluster')
        status = request.POST.get('is_active')
    
        if LibFundSource.objects.filter(name=fundsource):
            return JsonResponse({'data': 'error'})
        else:
            add = LibFundSource(
                name= fundsource,cluster = cluster_name, is_active = status)
            add.save()
        return JsonResponse({'data': 'success'})
        
     
@csrf_exempt
def updatefundsource(request):
    if request.method == 'POST':
        fundsource_id = request.POST.get('fundsource_id')
        cluster_name = request.POST.get('cluster')
        fundsource = request.POST.get('fundsource')
        status = request.POST.get('is_active')

        if LibFundSource.objects.filter(name=fundsource).exclude(id=fundsource_id):
            return JsonResponse({'data': 'error'})
        else:
            LibFundSource.objects.filter(id=fundsource_id).update(name=fundsource,cluster =cluster_name, is_active=status)
            return JsonResponse({'data': 'success'})
    

@csrf_exempt
def fundsourcedetails(request):
    fs_id = request.POST.get('fund_source')
    qs_list = list(
         (LibFundSource.objects
             .filter(id=fs_id)
             .values('name','cluster','is_active')
         )
    )
    return JsonResponse({'data': qs_list})
    

def uacs(request):
    context = {
		'uacs' : LibUacs.objects.filter().order_by('created_at')
	}
    return render(request, 'admin/uacs.html', context)

@csrf_exempt
def adduacs(request):
    if request.method == 'POST':
        uacs_code = request.POST.get('uacscode')
        uacs_description = request.POST.get('uacsdescription')
        status = request.POST.get('is_active')

        if LibUacs.objects.filter(code=uacs_code):
            return JsonResponse({'data': 'error'})
        else:
            add = LibUacs(
                code= uacs_code,description=uacs_description, is_active = status)
            add.save()
        return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updateuacs(request):
    if request.method == 'POST':
        uacs_id = request.POST.get('uacs_id')
        uacs_code = request.POST.get('uacscode')
        uacs_description = request.POST.get('uacsdescription')
        status = request.POST.get('is_active')

        if LibUacs.objects.filter(code=uacs_code).exclude(id=uacs_id):
            return JsonResponse({'data': 'error'})
        else:
            LibUacs.objects.filter(id=uacs_id).update(code=uacs_code,description = uacs_description, is_active=status)
            return JsonResponse({'data': 'success'})
    

@csrf_exempt
def uacsdetails(request):
    uacs_id = request.POST.get('uacs')
    qs_list = list(
         (LibUacs.objects
             .filter(id=uacs_id)
             .values('code','description','is_active')
         )
    )
    return JsonResponse({'data': qs_list})
    

def units(request):
    context = {
		'units' : LibUnits.objects.filter().order_by('created_at')
	}
    return render(request, 'admin/units.html', context)

@csrf_exempt
def addunits(request):
    if request.method == 'POST':
        units_name = request.POST.get('unitsname')
        status = request.POST.get('is_active')
    
        if LibUnits.objects.filter(name=units_name):
            return JsonResponse({'data': 'error'})
        else:
            add = LibUnits(
                name= units_name, is_active = status)
            add.save()
        return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updateunits(request):
    if request.method == 'POST':
        units_id = request.POST.get('units_id')
        unit_name = request.POST.get('unitsname')
        status = request.POST.get('is_active')

        if LibUnits.objects.filter(name=unit_name).exclude(id=units_id):
            return JsonResponse({'data': 'error'})
        else:
            LibUnits.objects.filter(id=units_id).update(name=unit_name, is_active=status)
            return JsonResponse({'data': 'success'})
        

@csrf_exempt
def unitdetails(request):
    unit_id = request.POST.get('units_id')
    qs_list = list(
         (LibUnits.objects
             .filter(id=unit_id)
             .values('name','is_active')
         )
    )
    return JsonResponse({'data': qs_list})


