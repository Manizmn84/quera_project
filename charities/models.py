from django.db import models
from accounts.models import User

class Benefactor(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=[
        (0,'Intremediate'),
        (1, 'Midlevel'),
        (2, 'Pro')
    ],default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)
    pass


class Charity(models.Model):
    pass


class Task(models.Model):
    pass
