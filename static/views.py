from django.http import HttpResponse
from django.shortcuts import render

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