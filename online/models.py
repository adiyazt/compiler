from django.db import models
import uuid

class File(models.Model):
    id = models.CharField(
        default=str(uuid.uuid4), primary_key=True, max_length=64
    )
    code = models.TextField(
        max_length=1024
    ) 
    dir = models.CharField(
        max_length=64, blank=True
    )
    name = models.CharField(
        max_length=64
    )
    user_id = models.CharField(
        max_length=64
    )

class User(models.Model):
    id = models.CharField(
        default=str(uuid.uuid4), primary_key=True, max_length=64
    )
    login = models.CharField(
        max_length=64
    )
    password = models.CharField(
        max_length=64
    )