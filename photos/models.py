from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

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
        self.delete()

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

    def filter_by_category(self):
        pass
    
    def search_image(self):
        pass

    def __str__(self):
        return self.description