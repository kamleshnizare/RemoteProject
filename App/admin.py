from django.contrib import admin
from .models import User

# create start admin here
class UserAdmin(admin.ModelAdmin):
    list_display = ['userID','email','username','password']

admin.site.register(User,UserAdmin)