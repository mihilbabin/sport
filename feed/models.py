import os
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils import timezone
from unidecode import unidecode
from .managers import PublishedManager
from .utils import get_upload_location


class CommonInfo(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Редагується'),
        ('published', 'Опубліковано')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news', default=1, verbose_name='користувач')
    image = models.ImageField(blank=True, null=True, upload_to=get_upload_location, verbose_name='зображення')
    title = models.CharField(max_length=200, unique=True, db_index=True, verbose_name="назва")
    content = models.TextField(verbose_name="зміст")
    slug = models.SlugField(max_length=140, blank=True, unique=True, verbose_name="URL")
    views = models.PositiveIntegerField(default=0, verbose_name="кількість переглядів")
    publish_date = models.DateTimeField(default=timezone.now, verbose_name="дата публікації")
    created = models.DateTimeField(auto_now_add=True,verbose_name="створено")
    updated = models.DateTimeField(auto_now=True, verbose_name="редаговано")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="статус")

    objects = models.Manager()
    published = PublishedManager()

    def delete(self, *args, **kwargs):
        self.image.delete(False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_published(self):
        if self.publish_date < timezone.now() and self.status == "published":
            return True
        return False
    is_published.boolean = True
    is_published.short_description = "Опубліковано на сайті"

    class Meta:
        abstract = True


class New(CommonInfo):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news', default=1, verbose_name='користувач')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.__create_slug()
        try:
            current_new = New.objects.get(pk=self.pk)
            if current_new.image != self.image:
                self.image.delete(False)
        except New.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    def __create_slug(self):
        slug = slugify(unidecode(self.title))
        if New.objects.filter(slug=slug).exists():
            slug = "{}-{}".format(slug, self.id)
        return slug

    def get_absolute_url(self):
        return reverse('feed:new_detail', args=(self.slug,))

    class Meta:
        verbose_name = 'новина'
        verbose_name_plural = 'Новини'
        ordering = ("-publish_date",)


class Article(CommonInfo):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='користувач')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='теги')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.__create_slug()
        try:
            current_new = Article.objects.get(pk=self.pk)
            if current_new.image != self.image:
                self.image.delete(False)
        except Article.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    def __create_slug(self):
        slug = slugify(unidecode(self.title))
        if Article.objects.filter(slug=slug).exists():
            slug = "{}-{}".format(slug, self.id)
        return slug

    class Meta:
        verbose_name = 'стаття'
        verbose_name_plural = 'статті'
        ordering = ("-publish_date",)

    def get_absolute_url(self):
        return reverse('feed:article_detail', args=(self.slug,))

class Tag(models.Model):
    name = models.CharField(max_length=25, db_index=True, verbose_name='тег')
    slug = models.SlugField(max_length=25, unique=True, verbose_name='URL', blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="створено")
    updated = models.DateTimeField(auto_now=True, verbose_name="редаговано")


    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if not self.slug:
            self.slug = slugify(unidecode(self.name))[:130]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("name",)
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name
