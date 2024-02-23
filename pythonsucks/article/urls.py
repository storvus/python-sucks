from django.urls import path

from pythonsucks.article.views import ArticleListView, ArticleDetailView

app_name = "article"

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("tag/<str:tag>/", ArticleListView.as_view(), name="tag"),
    path("article/<slug:slug>/", ArticleDetailView.as_view(), name="detail"),
]
