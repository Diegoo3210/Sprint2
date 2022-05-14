from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import profile, ChangePasswordView, passwordChange, ResetPasswordView
from django.contrib.auth import views as auth_views
 
urlpatterns = [
         path('', views.index, name ='index'),
         path('profile/', profile, name='users-profile'),
         path('password-change/', passwordChange, name='password_change'),
         path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
         path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
         path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]