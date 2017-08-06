from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
	all_album = Album.objects.all()
	context = {
		'all_album': all_album,
	}
 	return render(request, 'music/index.html', context)

def detail(request, album_id):
	return HttpResponse("<h2>Details for Album id : " + str(album_id) + "</h2>")
