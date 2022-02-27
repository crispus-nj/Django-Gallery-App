from django.shortcuts import render
from .models import Photo

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photos/index.html', context)

def photo(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {'photos': photos}
    return render(request, 'photos/photo.html', context)