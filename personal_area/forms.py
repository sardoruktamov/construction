from django import forms
from sotuvapp.models import Elon
from django.contrib.auth.models import User


#shaxsiy Kabinet formasi
class UserAccountForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'name':'first_name',
            'class':'form-control',
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'name':'last_name',
            'class':'form-control',
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'name':'email',
            'class':'form-control',
        })
    )
    
# Elon berish formasi
class ElonForm(forms.ModelForm):
    class Meta:
        model = Elon
        fields = ['rasm1','metall', 'eskiNarx','hozirgiNarx','m2','rasm2','rasm3','qushimcha','sana']
        # fields = '__all__'
        # labels = {'rasm1':'Asosiy rasm','eskiNarx':'Eski narx','hozirgiNarx':'Hozirgi narx','m2':'m2','rasm2':'Qo`shimcha rasm','rasm3':'Qo`shimcha rasm','metall':'Metall turi','qushimcha':'Qo`shimcha ma`lumotlar','sana':'sana'}
        # widgets = {
        #     'eskiNarx':forms.TextInput(attrs={'class': 'form-control'}),
        #     'hozirgiNarx':forms.TextInput(attrs={'class': 'form-control'}),
        #     'm2':forms.TextInput(attrs={'class': 'form-control'}), 
        #     'qushimcha':forms.TextInput(attrs={'class': 'form-control'}), 
        # }