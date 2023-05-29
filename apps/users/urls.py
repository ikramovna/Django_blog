from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from django.urls import path

from apps.users.views import (RegisterView, LogoutView, LoginView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('reset-password',
         PasswordResetView.as_view(
             template_name='apps/auth/password_reset.html'
         ),
         name='reset_password'),
    path('reset-password-done',
         PasswordResetDoneView.as_view(
             template_name='apps/auth/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset-password/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='apps/auth/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset-password-complete',
         PasswordResetCompleteView.as_view(
             template_name='apps/auth/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
