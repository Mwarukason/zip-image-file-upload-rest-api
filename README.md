# zip-image-file-upload-rest-api
uploading zip image file using rest api

This z simple REST API app for uploading single image and zip files using rest api, and provide links to download with unique file uploaded. The files will be saved into "uploaded_media_files"


## Quick Start
Installation Steps if you want to try it out
```bash
git clone https://github.com/Mwarukason/zip-image-file-upload-rest-api.git
cd zip-image-file-upload-rest-api


cd zip-image-file-upload-rest-api

python manage.py runserver # starts the server

open browser and go to link:
 http://127.0.0.1:8000/images/

Tested file:
-Choose the zip/image file (unique),
-Click POST,
-Link will be on top,


## REQUIREMENTS:
-Python 3.4+
-Django 1.11
-Django Rest Framework 3.5
-Pillow
