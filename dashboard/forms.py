from django import forms
from dashboard import views, models
from .models import *
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_email', 'account_password', 'account_started', 'account_ended', 'account_tl_count']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email','profile_name', 'profile_password', 'profile_bought_for', 'owner']
        owner = forms.ModelChoiceField(queryset=Customer.objects.all())

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['owner'].widget.attrs.update({'class': 'form-select mb3',
                                    'aria-label': '.form-select-lg example'
                                  })
            self.fields['email'].widget.attrs.update({'class': 'form-select mb3',
                                    'aria-label': '.form-select-lg example'
                                  })