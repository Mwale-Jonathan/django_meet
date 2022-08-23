from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages


def logout_message(sender, user, request, **kwargs):
	messages.info(request, 'You have been successifully logged out.')


def login_message(sender, user, request, **kwargs):
	messages.success(request, f'Welcome back {request.user.username}.')


user_logged_out.connect(logout_message)
user_logged_in.connect(login_message)
