from django.conf.urls import patterns,url
from my_app import views

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^successful/$', views.successful, name='successful'),
        url(r'^success/$', views.success, name='success'),
       
)

