import random
from unidecode import unidecode
from django.utils.text import slugify
from django.db import models
from django.core.urlresolvers import reverse_lazy
from .managers import PublishedManager, RandomManager

def get_upload_location(instance, filename):
    return "{}/{}/{}".format(instance.__class__.__name__, instance.album.slug, filename)


class Album(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Редагується'),
        ('published', 'Опубліковано')
    )
    title = models.CharField(max_length=64, db_index=True, verbose_name='Назва')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата створення')
    slug = models.SlugField(max_length=140, blank=True, unique=True, verbose_name="URL")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="статус")
    objects = models.Manager()
    published = PublishedManager()

    def count(self):
        return self.photos.count()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'альбом'
        verbose_name_plural = 'альбоми'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.__create_slug()
        super().save(*args, **kwargs)

    def __create_slug(self):
        slug = slugify(unidecode(self.title))
        if Album.objects.filter(slug=slug).exists():
            slug = "{}-{}".format(slug, random.randint(1, len(slug)))
        return slug

    def get_absolute_url(self):
        return reverse_lazy('gallery:album_detail', args=(self.slug,))


    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=64, db_index=True, verbose_name='Назва')
    image = models.ImageField(upload_to=get_upload_location, verbose_name='зображення')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата створення')
    album = models.ForeignKey(Album, related_name='photos')
    objects = RandomManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def save(self, *args, **kwargs):
        try:
            current_photo = Photo.objects.get(pk=self.pk)
            if current_photo.image != self.image:
                print("lel")
                self.image.delete(False)
        except Photo.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title



class Video(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Редагується'),
        ('published', 'Опубліковано')
    )
    title = models.CharField(max_length=64, db_index=True, verbose_name='Назва')
    url = models.URLField(verbose_name='URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата створення')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="статус")
    objects = models.Manager()
    published = PublishedManager()
    def __str__(self):
        return self.title


    class Meta:
        ordering = ('-created',)
        verbose_name = 'відео'
        verbose_name_plural = 'відео'
