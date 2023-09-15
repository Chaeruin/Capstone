from django.contrib import admin
from main.models import Member, Result, ImageUpload

# Register your models here.
class MemberAdmin( admin.ModelAdmin ) :
    list_display = ( "no", "name", "id", "phone", "email", "pw")
admin.site.register( Member, MemberAdmin )

class ResultAdmin( admin.ModelAdmin ):
    list_display = ( "no", "result", "date_time", "humidity", "temp")
admin.site.register( Result,ResultAdmin )

class ImageUploadAdmin( admin.ModelAdmin ):
    list_display = ( "no", "image")
admin.site.register( ImageUpload, ImageUploadAdmin )