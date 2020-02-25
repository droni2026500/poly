# coding: utf-8
from django import forms
from app.models import Doctor, Reception
from django.contrib.admin import widgets


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ('date','time','patient_name','patient_info','polis')

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.HiddenInput()
        self.fields['polis'].widget = forms.Textarea(attrs={'cols': 30, 'rows': 1})
        self.fields['polis'].label = 'Ваш полис (16 цифр)'
        self.fields['patient_info'].widget = forms.Textarea(attrs={'cols': 60, 'rows': 8})
        self.fields['patient_info'].label = 'Что вас беспокоит'
