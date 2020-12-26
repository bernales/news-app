# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


#extend the UserAdmin class so that it  uses the  new CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ] # new
    fieldsets = UserAdmin.fieldsets + ( # new
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
        (None, {'fields': ('age',)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)