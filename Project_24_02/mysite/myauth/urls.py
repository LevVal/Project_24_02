from django.urls import path
from django.contrib.auth.views import LoginView


from .views import login_view

app_name = "myauth"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="myauth/login.html"), name="login"),
]