from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50)
    resume_info = models.JSONField(null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)

    def __str__(self) -> str:
        return self.email + " " + self.resume_info