from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("", views.landing, name="landing"),
    path("sign-up", views.sign_up, name="sign-up")
]
