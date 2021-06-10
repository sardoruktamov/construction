from django import forms
from .models import Elon, UserDetail
from django.contrib.auth.models import User


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name':'Ism', 'last_name':'Familya', 'email':'Elektron pochta'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['mobile', 'image','manzil', 'facebook','tiktok','telegram','instagram']
        labels = {'mobile':'Tel','image':'Profil rasmi'}
        widgets = {
            # 'rasm1':forms.FileInput(attrs={'class': 'form-control'}),
            'mobile':forms.TextInput(attrs={'class': 'form-control'}),
            'manzil':forms.TextInput(attrs={'class': 'form-control'}),
            'facebook':forms.TextInput(attrs={'class': 'form-control','placeholder':'https://www.facebook.com/username'}),
            'tiktok':forms.TextInput(attrs={'class': 'form-control','placeholder':'https://www..com/'}),
            'telegram':forms.TextInput(attrs={'class': 'form-control','placeholder':'https://www.te.ru/username'}),
            'instagram':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'https://www.ig.me/username'}),
        }

class SubscribeForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'email',
            'placeholder':'Emailni kiriting',
            'id':'emailtext',
            'required':'required',
            'name':'subscribe'
        })
    )

# Elon berish formasi
class ElonlarForm(forms.ModelForm):
    class Meta:
        model = Elon
        fields = ['rasm1','metall', 'eskiNarx','hozirgiNarx','m2','rasm2','rasm3','qushimcha','sana']
        labels = {'rasm1':'Asosiy rasm','metall':'Metall turi','eskiNarx':'Eski narx','hozirgiNarx':'Hozirgi narx','m2':'m2','rasm2':'Qo`shimcha rasm 1','rasm3':'Qo`shimcha rasm 2','qushimcha':'Qo`shimcha ma`lumotlar','sana':'sana'}
        widgets = {
            # 'rasm1':forms.FileInput(attrs={'class': 'form-control'}),
            'metall':forms.Select(attrs={'class': 'form-select mb-3', 'aria-label':'Floating form-select-lg example'}),
            'eskiNarx':forms.TextInput(attrs={'class': 'form-control'}),
            'hozirgiNarx':forms.TextInput(attrs={'class': 'form-control'}),
            'm2':forms.TextInput(attrs={'class': 'form-control'}), 
            # 'rasm2':forms.FileInput(attrs={'class': 'form-control'}),
            # 'rasm3':forms.FileInput(attrs={'class': 'form-control'}),
            'qushimcha':forms.TextInput(attrs={'class': 'form-control'}), 
            'sana':forms.DateInput(attrs={'class': 'form-control'}), 
        }