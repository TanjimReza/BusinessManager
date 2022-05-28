import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from progressbar import progressbar
from .models import *
from .forms import *
from datetime import date,timedelta


# Create your views here.

def dashboard(request):
    
    print("\n\n\n\n\n")
    context = {
        'profile_names':[],
        'accounts':[(account.account_email,account.account_started, account.account_ended) for account in Account.objects.all()],
    }
    print("\n\n\n\n\n")
    
    for profile in Profile.objects.all():
        print(profile.profile_name)
        print(profile.email_id)
        print(profile.profile_ends)
    
        if (date.today() + timedelta(days=3)) >= profile.profile_ends:
            danger = "badge bg-danger"
            info = (profile.profile_name, profile.email_id, profile.profile_ends,danger)
            context['profile_names'].append(info)
            
        else: 
            success = "badge bg-success"
            info = (profile.profile_name, profile.email_id, profile.profile_ends,success)
            context['profile_names'].append(info)
    
    print(context)
    return render(request, 'dashboard/index.html', context=context)
    
def status(request):
    return redirect('/')

def accounts(request):
    return redirect('/')

def customers(request):
    return redirect('/')

def addcost(request):
    return render(request, 'dashboard/add-cost.html')

def addprofit(request):
    return render(request, 'dashboard/add-profit.html')
#* DONE ADD ACCOUNT*#
def addaccount(request):

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            print("Form Data Valid!")
            result = form.save()
            context = {'success': True}
            return render(request, 
                     'dashboard/add-account.html',
                     context = context)
    
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

        context = {'form': form}
        return render(request, 'dashboard/add-account.html', context = context)
#* Renew Profile Done *#
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
        return redirect('success', name=request.POST.get('profile_name'), email=request.POST.get('email'), password=request.POST.get('profile_password'), started=request.POST.get('profile_created'), ends=request.POST.get('profile_ends'))
    
    else: 
        form = ProfileForm() 
        context = {'form': form}
        return render(request, 'dashboard/new-profile.html', context = context)
    
def renewprofile(request):
    form = ProfileUpdateForm()
    if request.method == "POST":
        print("POST REQUEST 3")
        print(request.POST)
        return redirect('updateprofile', id=request.POST.get('profile'))
    
    context = {'get_profile': True,
                    'form': form,
                    }
    return render(request, 'dashboard/renew-profile.html', context = context)
        


def updateprofile(request, id):
    print("\n\n UPDATE")
    form2 = ProfileForm(instance=Profile.objects.get(pk=id))
    if request.method == "GET":
        form2 = ProfileForm(instance=Profile.objects.get(pk=id))
    
    
    if request.method == "POST":
        form2 = ProfileForm(request.POST, instance=Profile.objects.get(pk=id))
        if form2.is_valid():
            form2.save()
            print(form2.data)
            print("SAVED FROM")
            return redirect('updateprofile', id=id)
        
        else: 
            print("\n\n INAVLID FORM")
            print(form2.errors)
    context = {
                'form2': form2,
              }
    
    return render(request, 'dashboard/update_profile.html', context = context)


def success(request,name="Profile", email="tanjim.netflix.0@gmail.com", password="1234", started="2022-05-02",ends="2022-05-03"):
    
    return render(request, 'dashboard/success.html', context={'name':name, 'email':email, 'password':password, 'started':started, 'ends':ends})



def removeaccount(request):
    return render(request, 'dashboard/remove-account.html')

def addcustomer(request):
    
    form = CustomerForm()
    
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            print("Form Data Valid!")
            form.save()
            return redirect('/')
                        

    
    context = {'form': form}
    return render(request, 'dashboard/add-customer.html', context=context)


def manageprofiles(request):
    return render(request, 'dashboard/manage-profiles.html')

def updatecredit(request):
    return render(request, 'dashboard/update-credit.html')

def demo(request):
    return render(request, 'dashboard/demo.html')
def demo2(request):
    return render(request, 'dashboard/demo2.html')