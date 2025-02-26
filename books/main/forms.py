from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, PasswordInput, CharField, ImageField

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """ form from class based view """

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'telephone')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')


class UserProfileForm(ModelForm):
    img = ImageField(required=False, label="Загрузить изображение")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'telephone', 'img']


class RegistrationForm(ModelForm):
    password = CharField(widget=PasswordInput)
    password_confirm = CharField(widget=PasswordInput, label="Подтверждение пароля")
    img = ImageField(required=False, label="Загрузить изображение")

    class Meta:
        model = CustomUser
        fields = ['img', 'username', 'email', 'first_name', 'last_name', 'telephone', 'address', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Пароли не совпадают.")

        return cleaned_data
