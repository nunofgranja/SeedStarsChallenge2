from django.db import models

class Entity(models.Model):
    entity_name = models.CharField(max_length=200)
    entity_email = models.EmailField(max_length=200)
    def __str__(self):
        return self.entity_name