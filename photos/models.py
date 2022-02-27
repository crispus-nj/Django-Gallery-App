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

class Photos(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.description