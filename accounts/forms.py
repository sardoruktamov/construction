from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Login',
        widget=forms.TextInput(attrs={
            'name':'username',
            'class':'form-control',
            'id':'exampleInputEmail1',
            'aria-describedby':'emailHelp',
            'placeholder':'Loginni kiriting..',
            'required':'required'
        })
    )

    password = forms.CharField(
        max_length=30,
        label='Parol',
        widget=forms.PasswordInput(attrs={
            'name':'password',
            'class':'form-control',
            'id':'exampleInputPassword1',
            'placeholder':'Parolni kiriting..',
            'required':'required'
        })
    )

class RegistrForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'first_name',
            'class':'form-control',
            'id':'firstInput',
            'placeholder':'Ismingizni kiriting..',
            'required':'required'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'last_name',
            'class':'form-control',
            'id':'lastInput',
            'placeholder':'familyangizni kiriting..',
            'required':'required'
        })
    )
    
    email = forms.EmailField(
        max_length=40,
        widget=forms.EmailInput(attrs={
            'name':'email',
            'class':'form-control',
            'id':'emailInput',
            'placeholder':'elektronpochta@gmail.com',
            'required':'required'
        })
    )
    
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'username',
            'class':'form-control',
            'id':'usernameInput',
            'placeholder':'Loginni kiriting va eslab qoling..',
            'required':'required'
        })
    )
    
    password1 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'name':'password1',
            'class':'form-control',
            'id':'InputPassword',
            'placeholder':'Parolni kiriting va eslab qoling..',
            'required':'required'
        })
    )
    
    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'name':'password2',
            'class':'form-control',
            'id':'InputPassword',
            'placeholder':'Parolni qayta kiriting..',
            'required':'required'
        })
    )

    