from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^getlist/', views.getlist)
]