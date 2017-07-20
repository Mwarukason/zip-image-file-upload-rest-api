from django.conf.urls import url, include
from rest_framework import routers
from image_upload_rest_app.viewsets import ImagesViewSet


router = routers.DefaultRouter()
# let router knw new endpoint '/api/images'
router.register('images', ImagesViewSet, 'images')


# automatic URL routing for API.
# login URLs for the browsable API included.
urlpatterns = [
    url(r'^', include(router.urls)),
]
