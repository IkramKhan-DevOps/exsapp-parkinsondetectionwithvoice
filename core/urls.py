"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from dj_rest_auth.registration.views import VerifyEmailView
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from src.accounts.views import CustomRegisterAccountView, GoogleLoginView
from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    # ADMIN/ROOT APPLICATION
    path('', TemplateView.as_view(template_name='website/home.html')),
    path('admin/', admin.site.urls),

    # WEBSITE APPLICATION --------------------------------------------------------------------------------
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),

    path(
        'reset/password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
        name='reset_password'
    ),
    path(
        'reset/password/sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
        name='password_reset_confirm'
    ),
    path(
        'reset/password/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name='password_reset_complete'
    ),

    # REST API -------------------------------------------------------------------------------------------
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', CustomRegisterAccountView.as_view(), name='account_create_new_user'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),name='account_confirm_email'),
    path('auth/google/', GoogleLoginView.as_view(), name='google-login-view'),

    path('api/', include('src.api.urls', namespace='api')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
