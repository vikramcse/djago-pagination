from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^getlist/', views.getlist),
    url(r'^getlistwithdjangopagination/', views.get_list_with_django_pagination),
    url(r'^$', views.index),
]