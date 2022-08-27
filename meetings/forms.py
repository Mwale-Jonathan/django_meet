from django import forms
from .models import Meeting

class DateInput(forms.DateInput):
    input_type = 'date'

class MeetingForm(forms.ModelForm):
    # host = forms.fields.CharField(widget=forms.widgets.HiddenInput())
    date = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    start_time = forms.fields.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    end_time = forms.fields.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Meeting
        fields = ['host', 'channel', 'date', 'start_time', 'end_time']
