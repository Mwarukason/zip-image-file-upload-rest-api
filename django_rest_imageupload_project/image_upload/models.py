from django.db import models
import uuid
from django.db import models

# zip file upload  model
from zipfile import ZipFile
from django.contrib import messages


def format_uploaded_filename(instance, filename):
    # if is_zipfile(filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class ZipImageUploaded(models.Model):
    zip_file = models.FileField("CHOOSE ZIP FILE", unique=True,
    upload_to = format_uploaded_filename)
