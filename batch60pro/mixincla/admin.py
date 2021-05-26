from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from mixincla.models import Snippet


class AdminSnippet(admin.ModelAdmin):
    list_display = ['created','title','code','linenos','language','style']

admin.site.register(Snippet,AdminSnippet)
