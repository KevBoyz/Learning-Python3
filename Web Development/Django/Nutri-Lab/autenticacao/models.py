from django.db import models
from django.contrib.auth.models import User


class Ativacao(models.Model):
    token = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username
