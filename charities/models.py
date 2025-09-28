from django.db import models
from accounts.models import User 
from django.db.models import Q


class Benefactor(models.Model):
    
    exp_choices=(
        (0,'Intremediate'),
        (1, 'Midlevel'),
        (2, 'Pro')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(default = 0, choices = exp_choices)
    free_time_per_week = models.PositiveSmallIntegerField(default = 0)
    pass


class Charity(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    pass


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        queryset = self.filter(charity__user__id = user.id)
        return queryset

    def related_tasks_to_benefactor(self, user):
        queryset = self.filter(assigned_benefactor__user__id = user.id)
        return queryset

    def all_related_tasks_to_user(self, user):
        return self.filter(
            Q(state= 'P') |
            Q(charity__user__id= user.id) |
            Q(assigned_benefactor__user__id= user.id))


class Task(models.Model):
    
    objects = TaskManager()
    
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    state_choices = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete= models.SET_NULL, null= True, blank= True)
    charity = models.ForeignKey(Charity, on_delete= models.CASCADE)
    age_limit_form = models.IntegerField(null= True, blank= True)
    age_limit_to = models.IntegerField(null= True, blank= True)
    date = models.DateField(null= True, blank= True)
    description = models.TextField(null= True, blank= True)
    gender_limit = models.CharField(choices= gender_choices, max_length=1, null= True, blank= True)
    state = models.CharField(choices= state_choices, max_length=50, default= 'P')
    title = models.CharField(max_length= 60)
    pass
