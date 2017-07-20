#from django.core import serializers
from rest_framework import serializers
from image_upload.models import ZipImageUploaded
    #Import ImageUploaded model


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipImageUploaded
        #fields = ('pk', 'image',)
        fields = ('pk', 'zip_file',)
        # It serializes the primary
        # key-pk and the image field
        # It tells the DRF engine to serializes the fields 'pk' and image of model
