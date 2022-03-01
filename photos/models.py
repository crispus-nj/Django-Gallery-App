from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def filter_by_location(cls, location):
        '''
        filter_by_location for filtering all the photos with the same location
        '''
        location = '';
        locate = Location.objects.filter(name = location)
        print("Location", locate)
        # return locate
        for loca in locate:
            location = loca
        return location

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    @classmethod
    def filter_by_category(cls, category):
        '''
        filter_by_category for filtering all the photos with the same category
        '''
        catg = '';
        catego = Category.objects.filter(name = category)
        print("category",catego)
        for cate in catego:
            catg = cate
        return catg


    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete

    def update_image(self):
        pass

    @classmethod
    def get_image_by_id(cls, pk):
        image = Photo.objects.get(id = pk)
        return image

    @classmethod
    def filter_by_location(cls, location):
        image = Location.objects.filter(name = location)
        # for image in image:
        #     image = image.location
        return image 

    
    def search_image(self):
        pass

    def __str__(self):
        return self.description