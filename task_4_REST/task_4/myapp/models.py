from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.IntegerField()
    committee = models.ForeignKey('Committee')

    def __str__(self):
        return self.name


class Committee(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
