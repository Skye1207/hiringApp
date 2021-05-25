from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("success/", views.success, name="success"),
    path("response/", views.response, name="response")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
