from django.db import models


class User(models.Model):
    names = models.CharField(max_length=200)
    last_names = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.names} {self.last_names}"
