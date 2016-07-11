from django.shortcuts import render, get_object_or_404
from django.conf import settings
from os import path

from .models import Meme

# Create your views here.

def home(request):
	return render(request, 'home.html')

def show_meme(request, meme):
	memeObject = get_object_or_404(Meme, slug=meme)
	with open(path.join(settings.MEME_DIR, "{}.md".format(meme)), "r") as memeFile:
		memeContent = memeFile.read()
	memeMarkup = memeContent #TODO
	context = {
		"title": memeObject.title,
		"content": memeMarkup
	}
	return render(request, 'meme.html', context)
