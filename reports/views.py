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


@csrf_exempt
def rsmi(request):
    return render(request, 'reports/rsmi.html')
  
@csrf_exempt
def ledger(request):
    return render(request, 'reports/ledger.html')
  
  

  

  




