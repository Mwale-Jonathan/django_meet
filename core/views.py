from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def landing(request):
    # messages.success(request, 'This is a message from django')
    return render(request, 'core/landing.html')


def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'base.html', context)
