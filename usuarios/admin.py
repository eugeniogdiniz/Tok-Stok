from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as adimin_auth_jdango
from .forms import UserChangeForms, UserCreationForm

@admin.register(Users)
class UserAdmin(adimin_auth_jdango.UserAdmin):
    form = UserChangeForms
    add_fom = UserCreationForm
    model = Users
    fieldsets = adimin_auth_jdango.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )



# Register your models here.
