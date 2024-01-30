from django.db import models
from djongo.models import ObjectIdField


class Statement(models.Model):
    _id = ObjectIdField(primary_key=True)  # Assuming it's an ObjectIdField
    created_at = models.DateTimeField()
    in_response_to = models.CharField(max_length=255)
    id = models.CharField(max_length=255, unique=True)
    persona = models.CharField(max_length=255)
    search_in_response_to = models.CharField(max_length=255)
    search_text = models.CharField(max_length=255)
    tags = models.JSONField()  # Assuming it's an array of strings
    text = models.TextField()

    def __str__(self):
        return self.text
    class Meta:
        db_table='statements'

