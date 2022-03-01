from django.test import TestCase
from .models import Category, Photo, Location

class CategoryTestClass(TestCase):
    # set up
    def setUp(self):
        self.category = Category(name="Pet")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name="Thika")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

class PhotoTestClass(TestCase):

    # set up method
    def setUp(self):
        '''
        setUp function creates the instance of class Photo
        '''
        self.category = Category.objects.create(name = 'Pet')
        self.location = Location.objects.create(name = 'Thika')
        self.crispus = Photo(category = self.category, location = self.location, image ='test.jpg', description="Nice pet")
        
    # Testing  instance
    def test_instance(self):
        
        self.assertTrue(isinstance(self.crispus, Photo))

