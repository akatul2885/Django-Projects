from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.first_name

