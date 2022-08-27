from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from meetings.models import Meeting

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect(reverse('lobby'))
    return render(request, 'core/landing.html')

@login_required
def lobby(request):
    context = {
        'title': 'Lobby',
        'meetings': Meeting.objects.all()
    }
    return render(request, 'core/lobby.html', context)
