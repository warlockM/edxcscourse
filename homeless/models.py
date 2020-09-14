from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 50)
    purpose = models.CharField(max_length = 500)

    def __str__(self):
        return f"{self.name}"
