from django.contrib.auth.models import User
from django.db import models


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_guest = models.BooleanField(default=False, blank=False)
    logged_in = models.BooleanField(default=False, blank=False)

    class Meta:
        db_table = "user_detail"
