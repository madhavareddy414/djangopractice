from django.conf.urls import url
from django.urls import path

from formTest import views

urlpatterns = [
    # url(r'^urltest/',views.appurlinfo)
    path(r'form/',views.studentinputview)
]