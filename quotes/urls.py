from django.contrib import admin
from django.urls import path
from .views import Tsitata


urlpatterns = [
    path('list/', Tsitata.as_view()),
    path('yangi-url/', Tsitata.as_view()),
]
