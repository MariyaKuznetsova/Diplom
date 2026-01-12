from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from diary.forms import BootstrapFormMixin
from users.models import User


class UserRegisterForm(BootstrapFormMixin, UserCreationForm):
    """Форма для регистрации пользователя"""
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserUpdateForm(BootstrapFormMixin, ModelForm):
    """Форма для редактирования пользователя"""
    class Meta:
        model = User
        fields = ["nik", "phone_number", "avatar", "country", "city", "myself"]
