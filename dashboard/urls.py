
from django.contrib import admin
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.dashboard, name='dashboard'),
    #! Dashboard URLs
    path('status',views.status, name='status'),
    path('accounts',views.accounts, name='accounts'),
    path('customers',views.customers, name='customers'),
    
    #! Netflix URLs
    path('addaccount',views.addaccount, name='addaccount'),
    path('removeaccount',views.removeaccount, name='removeaccount'),
    path('updatecredit',views.updatecredit, name='updatecredit'),
    path('manageprofiles',views.manageprofiles, name='manageprofiles'),
    
    #! Netflix-Sell URLs
    path('newprofile',views.newprofile, name='newprofile'),
    path('renewprofile',views.renewprofile, name='renewprofile'),
    path('updateprofile/<str:id>/',views.updateprofile, name='updateprofile'),
    path('addcustomer',views.addcustomer, name='addcustomer'),
    #! Finance URLs
    path('addcost',views.addcost, name='addcost'),
    path('addprofit',views.addprofit, name='addprofit'),
    
    
    #! DEMO URLs
    path('demo',views.demo, name='demo'),
    path('demo2',views.demo2, name='demo2'),
  
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
