
from django.db import models


class CustomUser(models.Model):

    email = models.CharField(max_length=80)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} >>> {self.email}'











