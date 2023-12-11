from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path("", include('pythonsucks.article.urls', namespace="article")),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
