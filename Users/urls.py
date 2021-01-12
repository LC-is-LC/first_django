from django.urls import path
from django.contrib.auth import views as django_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register, name='Register'),
    path('profile/', views.profile, name='profile'),
    # Django builtin views for login, logout, password reset, password reset done
    # as_view is to make them views with the template included
    path('login/', django_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', django_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('password-reset/', django_views.PasswordResetView.as_view(template_name='Users/password_reset.html'),
         name='password-reset'),
    path('password-reset/done/', django_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'),
         name='password_reset_done'),
    # the values inside the <> are the parameters that the site needs to be able to access that particular path
    path('password-reset-confirm/<uidb64>/<token>/',
         django_views.PasswordResetConfirmView.as_view(template_name='Users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         django_views.PasswordResetCompleteView.as_view(template_name='Users/password_reset_complete.html'),
         name='password_reset_complete')
]

# Add the media_root and url when in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)