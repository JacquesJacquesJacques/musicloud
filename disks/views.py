from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Album, Track

# Create your views here.


def home(request):
    albums = Album.objects.all
    return render(request, 'disks/home.html', {'albums': albums})


def album(request, id):
    album = get_object_or_404(Album, id=id)
    tracks = get_list_or_404(Track, album_id=id)
    return render(request, 'disks/album.html', {'tracks': tracks, 'album': album})


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

    title = query
    context = {'albums': albums, 'title': title}
    return render(request, 'disks/search.html', context)
