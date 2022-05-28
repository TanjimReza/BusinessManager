import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
        print(request)
        print(form)
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
        print(context)
        return render(request,
                      'dashboard/new-profile.html',
                      context= context)
    
    else: 
        form = ProfileForm() 
        print(request)
        context = {'form': form}
        return render(request, 'dashboard/new-profile.html', context = context)
    

def renewprofile(request):
    form = ProfileUpdateForm()
    if request.method == "POST":
        print("POST REQUEST 3")
        print(request.POST)
        profile_pk = request.POST.get('profile')
        if profile_pk is not None:
            profile = Profile.objects.get(pk=profile_pk)
            form2 = ProfileForm(instance=profile)
            context = {
                'form2': form2,
                'update': True,
                'owner': profile.owner,
            }
            # 
            return redirect('renewprofile2', id=profile_pk)
            # return render(request, 'dashboard/renew-profile.html', context = context)
    
    context = {'get_profile': True,
                    'form': form,
                    }
    return render(request, 'dashboard/renew-profile.html', context = context)
        


def renewprofile2(request, id):
    profile = Profile.objects.get(pk=id)
    print(profile)
    print(id)
    profile = Profile.objects.get(pk=id)
    form2 = ProfileForm(instance=profile)
    context = {
        'form2': form2,
        'update': True,
        'owner': profile.owner,
    }
    return render(request, 'dashboard/renew-profile.html', context=context)
    
    
    
    # if request.POST.get('profile') is None:
    #     print("POST REQUEST 4")
    #     print(request.POST)
    #     print(request.POST.get('profile'))
    #     form2 = ProfileForm(request.POST or None, instance=Profile.objects.get(id=request.POST.get('profile')))

    #     if form2.is_valid():
    #         print("Form 2 data VALID")
    #         form2.save()
    #         return HttpResponse("UPDATED")
    #     else: 
    #         print("Form 2 data INVALID")
    #         print(form2.errors.as_data)
    #         context = {'get_profile': True,
    #             'form': form,
    #             }

    #         return render(request, 'dashboard/renew-profile.html', context = context)


      


def removeaccount(request):
    return render(request, 'dashboard/remove-account.html')

def manageprofiles(request):
    return render(request, 'dashboard/manage-profiles.html')

def updatecredit(request):
    return render(request, 'dashboard/update-credit.html')

def demo(request):
    return render(request, 'dashboard/demo.html')
def demo2(request):
    return render(request, 'dashboard/demo2.html')