from rest_framework import viewsets, filters
from image_upload_rest_app.serializers import ImageSerializer
# importing the serializer
from image_upload.models import ZipImageUploaded
# importing model from image_upload app


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = ZipImageUploaded.objects.all()
    serializer_class = ImageSerializer

    # queryset used to serve data frm db to REST endpoint
