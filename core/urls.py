from django.contrib import admin
from django.urls import path

from google_ads.api import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
