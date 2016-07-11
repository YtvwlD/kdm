from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
	return render(request, 'home.html', {"current_version": settings.COMMIT})
