from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreateView, UserDetailView, UserUpdateView,
                         email_verification)

app_name = UsersConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="diary:record_list"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/edit/", UserUpdateView.as_view(), name="profile_edit"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
