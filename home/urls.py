"""fed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
) 

app_name = "home"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, {'template_name':'home/login.html'},name="login"),
    url(r'^logout/$', logout,{'template_name':'index.html'},name='logout'),
    url(r'^change-password/$',views.change_password, name="change_password"),

    url(r'^reset-password/$', password_reset, {'template_name':'home/reset_password.html',
                                                    'email_template_name':'home/reset_password_email.html',
                                                    'post_reset_redirect':'home:password_reset_done',
                                                    'from_email':'home@django.com',},name='password_reset'),

   
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'home/reset_password_done.html'},
                                                         name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm, {'template_name':'home/reset_password_confirm.html',
                              'post_reset_redirect': reverse_lazy('home:password_reset_complete')},
                              name='password_reset_confirm'),


    url(r'reset-password/complete/$', password_reset_complete,{'template_name':'home/reset_password_complete.html'}, name='password_reset_complete'),
                
    # url(r'^poll/', include('poll.urls')),
]
