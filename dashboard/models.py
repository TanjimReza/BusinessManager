from django.db import models
# Create your models here.
from datetime import datetime, timedelta

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey("Account", on_delete=models.SET_NULL, null=True)
    name = models.CharField(name="profile_name", max_length=100)
    password = models.CharField(name="profile_password", max_length=100)
    credit = models.IntegerField(name="profile_credit", default=0)
    created_at = models.DateField(name="profile_created", auto_now_add=True)
    ends_at = models.DateField(name="profile_ends", auto_now_add=True)
    bought_for = models.CharField(name="profile_bought_for",max_length=10)
    owner = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)
    profile_type = models.CharField(name="profile_type", max_length=100, default="NonVPN")
    def __str__(self):
        return str(self.profile_name)
    class Meta:
        db_table = 'profile'

class Account(models.Model):
    account_email = models.EmailField(name="account_email", max_length=100,primary_key=True)
    account_password = models.CharField(name="account_password", max_length=100)
    started_at = models.DateField(name="account_started", auto_now_add=False)
    ended_at = models.DateField(name="account_ended", auto_now=False)
    refil_count = models.IntegerField(name="account_refil_count", default=0)
    refil_date = models.DateField(name="account_refil_date", auto_now=True)
    tl_count = models.IntegerField(name="account_tl_count", default=0)
    profiles = models.ForeignKey("Profile", on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
        return str(self.account_email)
    
    class Meta:
        db_table = 'account'


class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(name="customer_name", max_length=100)
    customer_profiles = models.ManyToOneRel(field="profile",field_name="profiles", to="Profile", on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return str(self.customer_name)
    
    class Meta:
        db_table = 'customer'
        constraints = [ models.UniqueConstraint(fields=['customer_name','cid'], name='customer_name_unique') ]

class Profiles(models.Model):
    profile = models.OneToOneField("Profile", on_delete=models.CASCADE, primary_key=True)
    