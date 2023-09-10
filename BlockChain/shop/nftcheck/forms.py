from django import forms
from nftcheck.models import Checker
from django.utils import timezone


class PostForm(forms.ModelForm):
    class Meta:
        model = Checker
        fields = ('policyID', 'assetID', 'time_create', )
        widget = {
            'policyID': forms.Textarea(attrs={'class': 'form-control'}),
            'assetID': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class Send(forms.Form):
#     policyID = forms.CharField(max_length=100, widget = forms.TimeInput(attrs = {'class': 'policyID'}))
#     assetID = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class' : 'assetID'}))
#     time_create = forms.DateField()