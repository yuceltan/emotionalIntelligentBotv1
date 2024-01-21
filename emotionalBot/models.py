from django.db import models


class TrainData(models.Model):
    statement_text = models.TextField()

    def __str__(self):
        return self.statement_text

