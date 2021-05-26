from django.db import models

class Labour(models.Model):
    lname = models.CharField(max_length=125)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.name