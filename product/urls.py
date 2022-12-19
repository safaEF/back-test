from django.urls import path
from .views import  FileUploadView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
urlpatterns = [
    # path('', include(router.urls)),
    path('upload', FileUploadView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
