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
        # check_generic = False
        # generic_name = request.POST.get('companyname')
        # code_name = request.POST.get('code')
        # address_ = request.POST.get('address')
        # remarks = request.POST.get('remarks')
        # if Company.objects.filter(name=generic_name):
        #     return JsonResponse({'data': 'error'})
        # else:
        #     check_generic = True        
        # if check_generic:
        #     add = Company(
        #         name= generic_name, code = code_name, address = address_, remarks = remarks)
        #     add.save()
            return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updateresponsibilitycenter(request):
    # if request.method == 'POST':
    #     company_id = request.POST.get('company_id')
    #     company_name = request.POST.get('companyname')
    #     status = request.POST.get('is_active')
    #     code_name = request.POST.get('code')
    #     address_ = request.POST.get('address')
    #     remarks = request.POST.get('remarks')

    #     check_company = False
    #     if Company.objects.filter(name=company_name).exclude(id=company_id):
    #         return JsonResponse({'data': 'error'})
    #     else:
    #         check_company = True        
    #     if check_company:
    #         Company.objects.filter(id=company_id).update(name=company_name, is_active=status,code = code_name, address = address_, remarks = remarks)
            return JsonResponse({'data': 'success'})


def fundsource(request):
    context = {
		'fund_source' : LibFundSource.objects.filter().order_by('name')
	}
    return render(request, 'admin/fund_source.html', context)

@csrf_exempt
def addfundsource(request):
    if request.method == 'POST':
         return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updatefundsource(request):
    if request.method == 'POST':
         return JsonResponse({'data': 'success'})
    

def uacs(request):
    context = {
		'uacs' : LibUacs.objects.filter().order_by('created_at')
	}
    return render(request, 'admin/uacs.html', context)

@csrf_exempt
def adduacs(request):
    if request.method == 'POST':
         return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updateuacs(request):
    if request.method == 'POST':
         return JsonResponse({'data': 'success'})
    

def units(request):
    context = {
		'units' : LibUnits.objects.filter().order_by('created_at')
	}
    return render(request, 'admin/units.html', context)

@csrf_exempt
def addunits(request):
    if request.method == 'POST':
        generic_name = request.POST.get('companyname')
        code_name = request.POST.get('code')
        address_ = request.POST.get('address')
        remarks = request.POST.get('remarks')
        
        if LibUnits.objects.filter(name=generic_name):
            return JsonResponse({'data': 'error'})
        else:
            add = LibUnits(
                name= generic_name, code = code_name, address = address_, remarks = remarks)
            add.save()
        return JsonResponse({'data': 'success'})
        
@csrf_exempt
def updateunits(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        company_name = request.POST.get('companyname')
        status = request.POST.get('is_active')
        code_name = request.POST.get('code')
        address_ = request.POST.get('address')
        remarks = request.POST.get('remarks')

        if LibUnits.objects.filter(name=company_name).exclude(id=company_id):
            return JsonResponse({'data': 'error'})
        else:
            LibUnits.objects.filter(id=company_id).update(name=company_name, is_active=status,code = code_name, address = address_, remarks = remarks)
            return JsonResponse({'data': 'success'})