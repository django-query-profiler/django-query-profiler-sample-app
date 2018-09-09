from django.conf.urls import url
from . import views

app_name = 'food'

urlpatterns = [
    url(r'^order/$', views.order, name="order"),
    url(r'^$', views.homepage, name="home"),
]
