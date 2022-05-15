from django.db import models
# Create your models here.

class Profile(models.Model):
    email = models.ForeignKey("Account", on_delete=models.SET_NULL, null=True)
    name = models.CharField(name="profile_name", max_length=100, primary_key=True)
    password = models.CharField(name="profile_password", max_length=100)
    credit = models.IntegerField(name="profile_credit", default=0)
    created_at = models.DateField(name="profile_created", auto_now_add=True)
    ends_at = models.DateField(name="profile_ends", auto_now=True)
    bought_for = models.IntegerField(name="profile_bought_for", default=30)
    owner = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.profile_name)
    class Meta:
        db_table = 'profile'

class Account(models.Model):
    account_email = models.EmailField(name="account_email", max_length=100,primary_key=True)
    account_password = models.CharField(name="account_password", max_length=100)
    started_at = models.DateField(name="account_started", auto_now_add=True)
    ended_at = models.DateField(name="account_ended", auto_now=True)
    refil_count = models.IntegerField(name="account_refil_count", default=0)
    refil_date = models.DateField(name="account_refil_date", auto_now=True)
    tl_count = models.IntegerField(name="account_tl_count", default=0)
    profiles = models.ForeignKey("Profile", on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
        return str(self.account_email)
    
    class Meta:
        db_table = 'account'


class Customer(models.Model):
    name = models.CharField(name="customer_name", max_length=100, primary_key=True)
    customer_profiles = models.ForeignKey(Profile, name="customer_profiles", on_delete=models.SET_NULL,null=True)
    
    def __str__(self) -> str:
        return str(self.customer_name)
    
    class Meta:
        db_table = 'customer'