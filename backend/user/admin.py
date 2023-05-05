from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("no", "id", "name", "nickname", "pw", "email", "phone")
admin.site.register(User, UserAdmin)
