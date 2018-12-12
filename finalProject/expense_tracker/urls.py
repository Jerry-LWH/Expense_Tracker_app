from django.urls import path
from django.conf.urls import url
from . import views,ajax
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy,reverse


#set the namespace
app_name = 'expense_tracker'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    path('logout/',views.user_logout,name='logout'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^username_retrieve/$', views.username_retrieve, name='username_retrieve'),
    url('settings/', views.user_settings, name='settings'),
    url('schema.html/', views.schema, name='schema'),

    #new main page and envelop page
    url('main/$',views.main_page,name='main'),
    url('envelop/$', views.envelop, name = 'envelop'),
    url('ajax/',ajax.ajax_request,name ='ajax_request' ),
    #url(r'^reset-password/$',PasswordResetView.as_view(), name='reset_password'),
    #url(r'^reset-password/confirm/$', PasswordResetConfirmView.as_view(),name='password_reset_confirm')

    #password retrieval
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    #url(r'^password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    url(r'^password-reset/done/$', views.reset_done , name ='password_reset_done'),

    url(r'^reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^password-reset/complete/$', views.reset_complete, name='password_reset_complete'),
]
