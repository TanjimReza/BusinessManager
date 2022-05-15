import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/index.html')
    
def status(request):
    return render(request, 'dashboard/status.html')

def accounts(request):
    return render(request, 'dashboard/accounts.html')

def customers(request):
    return render(request, 'dashboard/customers.html')

def addcost(request):
    return render(request, 'dashboard/add-cost.html')

def addprofit(request):
    return render(request, 'dashboard/add-profit.html')

def addaccount(request):
    if request.method == "POST":
        print(request.POST)
        res = Account.objects.create(
            account_email = request.POST['account_email'],
            account_password = request.POST['account_password'],
            account_started = request.POST['account_started'],
            account_ended = request.POST['account_ended'],
            account_tl_count = request.POST['account_tl_count'],
        ) 
        print(res)
        print(request)
      
    return render(request, 'dashboard/add-account.html')

def removeaccount(request):
    return render(request, 'dashboard/remove-account.html')

def manageprofiles(request):
    return render(request, 'dashboard/manage-profiles.html')

def newprofile(request):
    return render(request, 'dashboard/new-profile.html')

def renewprofile(request):
    return render(request, 'dashboard/renew-profile.html')

def updatecredit(request):
    return render(request, 'dashboard/update-credit.html')

def demo(request):
    return render(request, 'dashboard/demo.html')
def demo2(request):
    return render(request, 'dashboard/demo2.html')