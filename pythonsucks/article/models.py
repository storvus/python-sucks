from ckeditor.fields import RichTextField
from django.db import models
from taggit.managers import TaggableManager


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255)
    body = RichTextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        ordering = ("-publish_date", )
        # indexes = ("slug", )

    def __str__(self):
        return self.title


