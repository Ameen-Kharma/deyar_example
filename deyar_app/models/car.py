

from django.db import models

from .base_model import BaseModel


class Car(BaseModel):
    class Meta:
        db_table = "car"

    name = models.CharField(max_length=255, null=True, default=None, blank=True)
