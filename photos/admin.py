from django.contrib import admin
from photos.models import Location, Category, Photos
# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Photos)