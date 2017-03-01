from random import sample, randint
from django.core.management import BaseCommand
from feed.models import New, Article, Tag
from elizabeth import Text

class Command(BaseCommand):
    help = "Seed tables of feed application"

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=100, type=int)

    def handle(self, *args, **options):
        count = options.get('count', 100)
        data = Text(locale='ru')
        tags = []
        for _ in range(10):
            try:
                tag = Tag.objects.create(name=data.word())
                tags.append(tag)
            except Exception as e:
                print(e)
        for i in range(count):
            try:
                New.objects.create(title="{} {}".format(data.sentence(), i), content=data.text(quantity=10))
                article = Article.objects.create(title="{} {}".format(data.sentence(), i), content=data.text(quantity=10))
                article.tags.add(*sample(tags, randint(0, len(tags))))
            except Exception as e:
                print(e)
