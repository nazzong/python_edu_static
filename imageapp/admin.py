from imageapp.models import ImageModel
from django.contrib import admin
from imageapp.models import ImageModel


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin) :
    
    pass