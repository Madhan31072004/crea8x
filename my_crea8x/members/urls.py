from django.contrib.auth.views import LoginView
from django.urls import path
from members.views import register

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
]
