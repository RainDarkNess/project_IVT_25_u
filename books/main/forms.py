from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, PasswordInput, CharField, ImageField, TextInput, Textarea

from .models import CustomUser, Genre, Books, Cover, Writer, Category, OrderRequests, Orderbooks


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
        fields = ['email', 'first_name', 'last_name', 'telephone', 'img', 'address']


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


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['namegenre']
        widgets = {
            'namegenre': TextInput(attrs={'placeholder': 'Введите название жанра', 'class': 'form-control'}),
        }


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'description', 'idcategory', 'idgenre', 'idwriter', 'idcover']
        widgets = {
            'description': Textarea(attrs={'rows': 4}),
        }


class CoverForm(ModelForm):
    img = ImageField(required=False, label="Загрузить изображение")

    class Meta:
        model = Cover
        fields = ['cover', 'img', 'descriptioncover']


class WriterForm(ModelForm):
    class Meta:
        model = Writer
        fields = ['lastname', 'firstname']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category']


class OrderRequestsForm(ModelForm):
    class Meta:
        model = OrderRequests
        fields = ['namebookrequest', 'booktorequest', 'category', 'address']
        widgets = {
            'namebookrequest': TextInput(attrs={'placeholder': 'Введите название книги'}),
            'address': TextInput(attrs={'placeholder': 'Введите адрес'}),
        }


class OrderbooksForm(ModelForm):
    class Meta:
        model = Orderbooks
        fields = ['bookone', 'booktwo', 'addressrequester', 'addressbookowner', 'status', 'useridone', 'useridtwo']
