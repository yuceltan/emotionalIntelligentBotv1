import json
from django.contrib import admin
from django import forms
from .models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display = ('text',)



admin.site.register(Statement, StatementAdmin)