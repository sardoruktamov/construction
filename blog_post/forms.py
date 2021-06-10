from django import forms
from .models import Commit, Post
from django.forms.widgets import TextInput, EmailInput, Textarea, FileInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','post_img','categorie','text_body1','post_img2','post_img3','text_body2','slug','tags','author']
        labels = {'title':'Sarlavha','post_img':'Asosiy rasm','categorie':'Kategoriya','text_body1':'Matn qism 1','post_img2':'Rasm 2','post_img3':'Rasm 3','text_body2':'Matn qism 2','slug':'Slug','tags':'Teglar','author':'Muallif'}        
        widgets = {
            'post_img':forms.FileInput(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'categorie':forms.Select(attrs={'class': 'form-select mb-3', 'aria-label':'Floating form-select-lg example'}),
            'text_body1':forms.Textarea(attrs={'class': 'form-control'}),
            'text_body2':forms.Textarea(attrs={'class': 'form-control'}),
            'slug':forms.TextInput(attrs={'class': 'form-control'}),
            'tags':forms.TextInput(attrs={'class': 'form-control'}), 
            'post_img2':forms.FileInput(attrs={'class': 'form-control'}),
            'post_img3':forms.FileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
        
    name = forms.CharField(widget = TextInput(attrs={
        'class':'form-control',
        'id':'name'
    
    }))

    email = forms.EmailField(widget = EmailInput(attrs={
        'class':'form-control',
        'id':'email'
    }))


    body = forms.CharField(widget = Textarea(attrs={
        'class':'form-control',
        'id':'message',
        'cols':'40',
        'rows':'2'
    }))

    class Meta:
        model = Commit
        fields = ['name','email','body']