from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    website = models.CharField(max_length=20)
    totalEmployees = models.IntegerField()

    def __str__(self):
        return self.name
