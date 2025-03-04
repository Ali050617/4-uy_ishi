from django.db import models


class Author(models.Model):
    objects = None
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name}{self.first_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
