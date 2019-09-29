from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    publish_year = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.title