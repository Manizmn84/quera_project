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
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    pass


class Task(models.Model):
    assigend_benefactor = models.ForeignKey(Benefactor , on_delete=models.SET_NULL , null=True)
    charity = models.ForeignKey(Charity)
    age_limit_form = models.IntegerField(blank=True , null=True)
    age_limit_to = models.IntegerField(blank=True , null=True)
    date = models.DateField(blank=True , null=True)
    description = models.TextField(blank=True , null=True)
    gender_limit = models.CharField(choices=[
        ("M","Male"),
        ("F","Female")
    ],blank=True,null=True)
    state = models.CharField(choices=[
        ("P","Pending"),
        ("W","Waiting"),
        ("A","Assigned"),
        ("D","Done")
    ],default="P")
    title = models.CharField(max_length=60)
    pass
