# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from seller.models import products


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name','last_name')

class UploadFileForm(forms.ModelForm):
	
	class Meta:
		model = products
		fields = ('picture',)

#class UserProfileForm(forms.ModelForm):
	#class Meta:
		#model = UserProfile
		#fields = ['picture', 'phone' ,'address', 'desc', 'video', 'timings']