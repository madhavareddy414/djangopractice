from django.contrib import admin
from testapp.models import Profile,Posts


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']
admin.site.register(Profile)
admin.site.register(Posts)