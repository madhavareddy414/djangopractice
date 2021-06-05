from django.contrib import admin
from testapp.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']
admin.site.register(Profile)