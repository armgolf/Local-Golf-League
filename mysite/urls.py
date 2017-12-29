from django.conf.urls import include, url
from django.contrib import admin
from golf import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from golf.forms import UserCreateForm
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url('^accounts/register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreateForm,
            success_url=reverse_lazy('landingpage')
    ), name='register'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'landingpage'}),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.landingpage, name='landingpage'),
    url(r'^rollups/$', views.rollups, name='rollups'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^customform/$', views.customform, name='customform'),  
]
