from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Q

class Event(models.Model):

    """
    - [x] Event name
    - [x] date
    - [x] description
    - [ ] type (optional)
    - [ ] photo (optional)
    - [x] participants
    - [x] required fund
    - [x] acquired fund
    - [x] Fund PPS
    - [x] branches
    - [x] batch
    - [ ] manager-1
    - [ ] manager-2 (optional)
    """

    name = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    deadline = models.DateField()
    description = models.TextField(blank=True)
    participants = models.PositiveIntegerField(blank=True)
    required_fund = models.DecimalField(max_digits=10, decimal_places=2)
    acquired_fund = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fund_pps = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    branch = models.ManyToManyField(Group, related_name='branch', limit_choices_to={'name__regex': r'^[a-zA-Z]{2}$'})
    batch = models.ManyToManyField(Group, related_name='batch', limit_choices_to={'name__regex': r'^\d{2}$'})
    manager_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_1')
    manager_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_2', blank=True)
    is_active = models.BooleanField(default=False)