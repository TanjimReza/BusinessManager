import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
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
#* DONE ADD ACCOUNT*#
def addaccount(request):

    if request.method == "POST":
        print(request.POST)
        form = AccountForm(request.POST)
        if form.is_valid():
            print("Form Data Valid!")
            result = form.save()
            print(result)
        else: 
            print("Form Data invalid!")
            print(form.errors)
            print(form.errors.as_data)
            #? SEND ERRORS BACK 
        context = {'errors': form.errors.as_data}
        return render(request, 
                     'dashboard/add-account.html',
                     context = context)
    
    
    else: 
        form = AccountForm() 
        print(request)
        print(form)
        context = {'form': form}
        return render(request, 'dashboard/add-account.html', context = context)

def newprofile(request):
    if request.method == "POST":
        print(request.POST)
        form = ProfileForm(request.POST)
        if form.is_valid():
            print("Form Data Valid!")
            result = form.save()
            print(result)
        else: 
            print("Form Data invalid!")
            print(form.errors.as_data)
        context = {'errors': form.errors.as_data}
        
        return render(request,
                      'dashboard/new-profile.html',
                      context= context)
    
    else: 
        form = ProfileForm() 
        print(request)
        context = {'form': form}
        return render(request, 'dashboard/new-profile.html', context = context)
    
      


def removeaccount(request):
    return render(request, 'dashboard/remove-account.html')

def manageprofiles(request):
    return render(request, 'dashboard/manage-profiles.html')

def renewprofile(request):
    return render(request, 'dashboard/renew-profile.html')

def updatecredit(request):
    return render(request, 'dashboard/update-credit.html')

def demo(request):
    return render(request, 'dashboard/demo.html')
def demo2(request):
    return render(request, 'dashboard/demo2.html')