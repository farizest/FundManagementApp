from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'deadline', 'description', 'participants',
                  'required_fund', 'acquired_fund', 'fund_pps',
                  'branch', 'batch', 'manager_1', 'manager_2']