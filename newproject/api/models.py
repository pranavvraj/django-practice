from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    metadata = JSONField(default=dict)

    class Meta:
        indexes = [
            models.Index(fields=['age'])
        ]

    def __str__(self):
        return self.name
    
    