from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #NOTE auth
    path('sign_up/', views.sign_up, name="sign_up"),
    path('logout/', views.logout, name="logout"),
    path('sign_in/', views.sign_in, name="sign_in"),
    #----
    #NOTE reset password
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"), name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_sent.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_form.html"), name="password_reset_confirm"),
    path('password_reset_complate', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_done.html"), name="password_reset_complate"),
    #----
    
]
