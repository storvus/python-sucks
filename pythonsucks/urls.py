from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('pythonsucks.article.urls', namespace="article")),
    path("ckeditor/", include("ckeditor_uploader.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
