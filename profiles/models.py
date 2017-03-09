import random
from datetime import date
from unidecode import unidecode
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from dateutil.relativedelta import relativedelta
from feed.utils import get_upload_location
from .managers import MemberManager

class Profile(models.Model):
    SEX_CHOICES = (
        ('m', 'Чоловіча'),
        ('f', 'Жіноча')
    )
    STATUS_CHOICES = (
        ('p', 'Учасник'),
        ('m', 'Член')
    )
    WEIGHT_CATEGORY_CHOICES = (
        ('lt44', 'менше 44кг'),
        ('lt48', 'менше 48кг'),
        ('lt52', 'менше 52кг'),
        ('lt56', 'менше 56кг'),
        ('lt60', 'менше 60кг'),
        ('lt67.5', 'менше 67.5кг'),
        ('lt75', 'менше 75кг'),
        ('lt82.5', 'менше 82.5кг'),
        ('lt90', 'менше 90кг'),
        ('lt100', 'менше 100кг'),
        ('gt100f', 'понад 100кг (жінки)'),
        ('lt110', 'менше 110кг'),
        ('lt125', 'менше 125кг'),
        ('lt140', 'менше 140кг'),
        ('gt140', 'понад 140кг')
    )
    full_name = models.CharField(max_length=100, verbose_name="Прізвище,ім'я та по-батькові")
    sex = models.CharField(max_length=1, verbose_name='стать', choices=SEX_CHOICES, default='m')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    city = models.CharField(max_length=64, verbose_name='місце проживання')
    bio = models.TextField()
    birth_date = models.DateField(verbose_name='дата народження')
    weight_category = models.CharField(max_length=10, verbose_name='вагова категорія', choices=WEIGHT_CATEGORY_CHOICES)
    age_category = models.CharField(max_length=35, blank=True, verbose_name='вікова категорія', editable=False)
    image = models.ImageField(verbose_name='Фото', blank=True, null=True, upload_to=get_upload_location)
    slug = models.SlugField(max_length=100, blank=True, unique=True, verbose_name='URL')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    objects = models.Manager()
    members = MemberManager()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.__create_slug()
        if not self.age_category:
            self.age_category = self.__create_age_category()
        try:
            current_profile = Profile.objects.get(pk=self.pk)
            if current_profile.image != self.image:
                self.image.delete(False)
        except Profile.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(False)
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profiles:profile_detail', args=(self.slug,))
    def __create_slug(self):
        slug = slugify(unidecode(self.full_name))
        if Profile.objects.filter(slug=slug).exists():
            slug = "{}-{}".format(slug, random.randint(1, len(slug)))
        return slug

    def __create_age_category(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        if age in range(10, 19):
            cat = 'Тінейджер'
        elif age in range(19, 24):
            cat = 'Юніор'
        elif age in range(24, 40):
            cat = 'Дорослий'
        elif age in range(40, 50):
            cat = 'Ветерани до 50 років'
        elif age in range(50, 60):
            cat = 'Ветерани до 60 років'
        elif age in range(60, 70):
            cat = 'Ветерани до 70 років'
        elif age > 70:
            cat = 'Ветерани від 70 років'
        return "{} (Вік: {})".format(cat, age)

    class Meta:
        ordering = ('full_name',)
        verbose_name = 'особова картка'
        verbose_name_plural = 'особові картки'
