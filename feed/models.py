from django.contrib.auth.models import User
from django.db import models


class UserDetail(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_detail"
