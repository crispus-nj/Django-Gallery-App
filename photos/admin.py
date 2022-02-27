from django.contrib import admin
from photos.models import Location, Category, Photo


admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Photo)