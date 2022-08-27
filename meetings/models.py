from django.db import models
from datetime import timedelta
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from accounts.models import User
from django.utils.timesince import timesince

# Create your models here.
class Meeting(models.Model):
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.CharField(max_length=100, unique=True, verbose_name='Title')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('room', kwargs={ 'slug': self.slug })

    def __str__(self):
        return self.channel

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.channel}')
        return super().save(*args, **kwargs)

    @property
    def duration(self):
        start_time = str(self.start_time).split(':')
        start_delta = timedelta(hours=int(start_time[0]), minutes=int(start_time[1]))
        end_time = str(self.end_time).split(':')
        end_delta = timedelta(hours=int(end_time[0]), minutes=int(end_time[1]))
        duration = (end_delta - start_delta)
        # print(dir(duration))
        return int((duration.total_seconds() // 60))





class MeetingMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    channel = models.CharField(max_length=200)

    class Meta:
        unique_together = ['name', 'uid', 'channel']

    def __str__(self):
        return self.name

