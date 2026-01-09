from django.contrib.auth.forms import UserCreationForm

from diary.forms import BootstrapFormMixin
from users.models import User


class UserRegisterForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2", "nik"]