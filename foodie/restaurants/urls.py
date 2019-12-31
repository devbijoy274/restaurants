from django.urls import include
from rest_framework.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='Home')
]
