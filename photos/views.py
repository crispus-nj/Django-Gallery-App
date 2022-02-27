from django.shortcuts import render
from .models import Photo, Category

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    category = Category.objects.all()
    context = {'photos': photos, 'category':category}
    return render(request, 'photos/index.html', context)

def photo(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {'photos': photos}
    return render(request, 'photos/photo.html', context)

def add_photo(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'photos/add_photo.html', context)