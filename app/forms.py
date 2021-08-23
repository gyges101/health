from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import *



class senderSms(ModelForm):

    class Meta:

        model = Rdv
        fields = '__all__'

class blogForm(ModelForm):
    class Meta:

        model = Blog
        fields = '__all__'
       