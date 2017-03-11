import random
from django.db import models

class RandomManager(models.Manager):
    def random(self, num=1):
        ids = list(self.get_queryset().values_list('id', flat=True))
        if len(ids) < num:
            num = len(ids)
        random_ids = random.sample(ids, num)
        return self.get_queryset().filter(id__in=random_ids)

class PublishedManager(RandomManager):

    def get_queryset(self):
        return super().get_queryset().filter(status='published')
