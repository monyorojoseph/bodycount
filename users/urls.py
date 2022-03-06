from django.urls import path, reverse_lazy
from django.contrib.auth import views
from .views import *

app_name = 'users'

urlpatterns = [
    # path('registration/', registration, name='registration'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('view_profile/', view_profile, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('close_account/', close_account, name='close_account'),
    
    # check username and mail
    path('check_mail/', check_mail, name='check_mail'),
    path('check_username/', check_username, name='check_username'),

    # password change
    path(
        "password_change/", views.PasswordChangeView.as_view(
            template_name = "users/password_change_form.html",
            success_url = reverse_lazy("users:password_change_done")
            ), 
            name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(template_name = "users/password_change_done.html"),
        name="password_change_done",
    ),

    # password reset
    path("password_reset/", views.PasswordResetView.as_view(
            template_name = "users/password_reset.html",
            success_url = reverse_lazy("users:password_reset_done"),
            email_template_name = "users/password_reset_email.html"
            ), 
        name="password_reset"
    ),
    path("password_reset/done/", views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name="password_reset_done"),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name = "users/password_reset_confirm.html",
            success_url = reverse_lazy("users:password_reset_complete")
            
        ),
        name="password_reset_confirm",
    ),
    path("reset/done/", views.PasswordResetCompleteView.as_view(template_name = "users/password_reset_complete.html"), name="password_reset_complete")
    ] 