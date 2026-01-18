from django.contrib import admin
from myapp.models import uploader
# Register your models here.
# admin.site.register(uploader)

@admin.register(uploader)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']
