"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from installers.views import installer_create_view
from customers.views import customer_create_view


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('account/', user_views.account, name='account'),
    path('jobs/', user_views.jobs),
    path('installations/', user_views.installations),
    path('quotes/', user_views.quotes),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',                                             #https://www.youtube.com/watch?v=-tyBEsHSv7w&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),               
    path('', include('blog.urls')), 

    #path('installers/', installer_detail_view),
    path('create/', installer_create_view),
    path('customers/', customer_create_view),
]


#https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#Title Headings In The Admin Page
#https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html
admin.site.site_header = "Swyft Energy Admin" #heading in admin login page 
admin.site.site_title = "Swyft Energy Admin Portal" #name on the tab
admin.site.index_title = "Welcome to Swyft Energy Portal"