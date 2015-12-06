# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class NameForm(forms.Form):
	your_name = forms.CharField(label="Your Name", max_length = 100)
