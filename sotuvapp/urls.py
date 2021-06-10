from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('properties/', views.properties, name='properties'),
    path('agents/', views.agents, name='agents'),
    path('oneannouncement/<int:blog_id>', views.oneannouncement, name='oneannouncement'),
    path('oneannouncement/edit/<int:blog_id>', views.edit_announcement, name='edit_announcement'),
    # path('oneannouncement/update/<int:id>', views.update_announcement, name='update_announcement'),
    path('oneannouncement/<int:blog_id>/delete', views.delete_announcement, name='delete_announcement'),
    #agentlar bergan elonlarni saralab olish
    path('agent/<int:id>', views.AgentDetailView.as_view(), name='agent-detail'),
    # path('add', views.add, name='add'),
    path('elements/', views.elements, name='elements'),
    path('contact/', views.contact, name='contact'),
    path('contact/contact_message', views.sendmail, name='sendmail'),
    path('', views.base, name='base'),
]