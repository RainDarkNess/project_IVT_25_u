from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    # everything else
    fieldsets = UserAdmin.fieldsets + (
    )


admin.site.register(CustomUser, CustomUserAdmin)
