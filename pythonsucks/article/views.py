from django.views.generic import ListView, DetailView

from pythonsucks.article.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if "tag" in self.kwargs:
            queryset = queryset.filter(tags__name__iexact=self.kwargs["tag"])
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"
