from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.myblog, name="blog"),
]
