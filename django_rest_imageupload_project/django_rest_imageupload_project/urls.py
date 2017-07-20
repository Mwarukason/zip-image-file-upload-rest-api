"""django_rest_imageupload_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
# Overcome the default serve media files
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url(r'^', include("image_upload_ui_app.urls")),
    url(r'^admin/', admin.site.urls),
    # anything going to /api gets redirected to the django rest API stuff
    url(r'^', include("image_upload_rest_app.urls")),
    # link rest urls frm rest app

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
