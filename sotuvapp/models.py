from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=13, verbose_name='Telefon', default='+')
    image = models.ImageField(upload_to='rasmlar/profil', default='rasmlar/profil/defoult.jpg')
    manzil = models.CharField(max_length=200, default="* viloyati, * tumani, * ko'chasi")
    facebook = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = ("Foydalanuvchi")
        verbose_name_plural = ("Foydalanuvchilar")

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    


class Elon(models.Model):
    rasm1       = models.ImageField(upload_to='rasmlar/elonlar/')
    eskiNarx    = models.CharField(max_length=10, null=True, blank=True)
    hozirgiNarx = models.CharField(max_length=10, null=True) 
    m2          = models.CharField(max_length=10, null=True) 
    rasm2       = models.ImageField(upload_to='rasmlar/elonlar/', blank=True)
    rasm3       = models.ImageField(upload_to='rasmlar/elonlar/', blank=True)
    ARMATURA    = 'Armatura'
    TRUBA       = 'Truba'
    KANTINER    = 'Kantiner'
    DAEWOO      = 'Daewoo'
    METALLTURI  = [
        (ARMATURA, 'Armatura'),
        (TRUBA, 'Truba'),
        (KANTINER, 'Kantiner'),
        (DAEWOO, 'Daewoo')
    ]
    metall      = models.CharField(max_length=100,choices=METALLTURI)
    qushimcha   = models.CharField(max_length=300,null=True, blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    sana        = models.DateField(default=datetime.now(), blank=True)
    vaqt        = models.TimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = ("Elon")
        verbose_name_plural = ("Elonlar")

    def __str__(self):
        return self.metall

class SubscribedUser(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.full_name
