from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    pass
