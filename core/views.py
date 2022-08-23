from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'core/landing.html')


def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'base.html', context)
