from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	email = models.EmailField(max_length=254, unique=True, verbose_name='Email Address')
	image = models.ImageField(upload_to='profile_pics', null=True, blank=True, verbose_name='Profile Picture')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', ]

	def __str__(self):
		return f'{self.first_name} {self.last_name} @{self.username}'

	@property
	def initials(self):
		if self.first_name and self.last_name:
			name = self.first_name[0] + self.last_name[0]
		else:
			name = self.username[0]
		return name
