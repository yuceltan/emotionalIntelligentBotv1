from chatterbot.ext.django_chatterbot.model_admin import StatementAdmin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from djongo.models import ObjectIdField
import json

from django.core.exceptions import ValidationError

from django.core.serializers.json import DjangoJSONEncoder

class Statement(models.Model):
    _id = ObjectIdField(primary_key=True)
    created_at = models.DateTimeField()
    in_response_to = models.CharField(max_length=255)
    id = models.CharField(max_length=255, unique=True)
    persona = models.CharField(max_length=255)
    search_in_response_to = models.CharField(max_length=255)
    search_text = models.CharField(max_length=255)
    #tags = models.JSONField(encoder=DjangoJSONEncoder)  # Use DjangoJSONEncoder
    text = models.TextField()
    feedback = models.CharField(max_length=50)

    class Meta:
        db_table = 'statements'




