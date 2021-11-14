from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='personal'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
    # path('oneannouncement/<int:blog_id>', views.oneannouncement, name='oneannouncement'),
]