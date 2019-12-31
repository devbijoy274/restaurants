from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restaurants/', include('foodie.restaurants.urls')),
]
