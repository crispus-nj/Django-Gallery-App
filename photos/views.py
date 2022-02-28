from django.shortcuts import render, redirect
from .models import Photo, Category, Location
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # t = request.GET.get('t') if request.GET.get('t') !=  None else ''
    # print(q)
    image = Photo.filter_by_location(location = q)
    print(image)
    for image in image:
        print("Erickooo",image)
    photos = Photo.objects.filter(Q(category__name__icontains = q) |
                                    Q(location__name__icontains = q)).order_by('-date_posted')
    category = Category.objects.all()
    context = {'photos': photos, 'category':category}
    return render(request, 'photos/index.html', context)

def photo(request, pk):
    photos = Photo.get_image_by_id(pk = pk)
    context = {'photos': photos}
    return render(request, 'photos/photo.html', context)

def add_photo(request):
    location = Location.objects.all()
    category = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        # print(data.get('location'))
        # if data['category'] != 'none' and data['location'] != 'none':
        #     category = Category.objects.get(id = data['category'])
        #     location = Location.objects.get(id = data['location'])
        # else:
        #     category = None
        #     location = None

        # photo = Photo.objects.create(
        #     category = data.get('category'),
        #     location = data.get('location'),
        #     image = image,
        #     description = data.get('description'),  
        # )
        return redirect('home')
    context = {'category':category, 'location':location}
    return render(request, 'photos/add_photo.html', context)