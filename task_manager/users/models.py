from django.db import models
# from django.contrib.auth.models import AbstractUser


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        # return self.get_full_name()
        return self.first_name