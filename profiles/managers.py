import random
from django.db import models
from django.utils import timezone

class MemberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='member')

    def random(self, num=2):
        ids = self.get_queryset().values_list('id', flat=True)
        random_ids = random.sample(ids, num)
        return self.get_queryset().filter(id__in=random_ids)
