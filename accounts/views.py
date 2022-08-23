from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, AccountUpdateForm
from django.contrib import messages

# Create your views here.
def signup(request):
	if request.user.is_authenticated:
		return redirect(reverse('landing'))

	form = SignupForm()

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			messages.success(request, f'{username}, your account has been created. You can now login.')
			return redirect(reverse('login'))

	context = {
		'title': 'Create your account now!!!',
		'form': form
	}
	return render(request, 'accounts/signup.html', context)


@login_required
def account(request):

	form = AccountUpdateForm(instance=request.user)

	if request.method == 'POST':
		form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your account has been updated successifully.')
			return redirect(reverse('account'))

	context = {
		'title': f"{request.user}",
		'form': form
	}
	return render(request, 'accounts/account.html', context)
