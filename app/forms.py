from django import forms
from django.forms import ModelForm
from .models import *



class senderSms(ModelForm):

    class Meta:

        model = Rdv
        fields = '__all__'
