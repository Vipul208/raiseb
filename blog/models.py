from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import Q
from django.utils.text import slugify

# Create your models here.


class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class BlogQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(title__icontains=query)
            | Q(description__contains=query)
            | Q(slug__icontains=query)
        )
        return self.filter(lookup)


class Blog(models.Model):

    title = models.CharField(
        max_length=255, unique=True, blank=False, null=False)
    slug = models.SlugField(default="", editable=False,
                            blank=False, max_length=255)

    image = models.ImageField()
    description = RichTextUploadingField(blank=True, null=True)
    date = models.DateField()
    objects = BlogManager()

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self, *args, **kwargs):
        kwargs = {"pk": self.id, "slug": self.slug}
        return f"/{self.id}-{self.slug}/"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
