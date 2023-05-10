from django.db import models

class UserInfo(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    surname = models.CharField(verbose_name="Surname", max_length=100)

    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = "UsersInfo"

    def __str__(self):
        return f"{self.surname}, {self.name}"