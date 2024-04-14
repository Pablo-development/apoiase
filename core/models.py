from django.db import models


# Create your models here.
class Pessoa(models.Model):
    username = models.CharField(max_length=30)
    useremail = models.EmailField()
    userfone = models.IntegerField()