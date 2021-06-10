from django.contrib import admin
from .models import Elon, UserDetail, ContactMessage
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(ContactMessage)

from .models import Elon
# Register your models here.
# admin.site.register(SubscribedUser)
# admin.site.register(Employee)
@admin.register(Elon) 
class PostModelElen(admin.ModelAdmin):
    list_display = ['id','metall', 'hozirgiNarx', 'm2', 'sana']