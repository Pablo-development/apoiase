from django.db import models


# Create your models here.
class Pessoa:
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.IntegerField

    def pessoa(self, username, useremail, userfone):
        self.nome = username
        self.email = useremail
        self.telefone = userfone
