from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
importing_episode = apps.get_model('play', 'Episode')


class AnimeFeed(Feed):
    title = "Latest Anime Feed"
    description = "Updates on the anime added and total anime present"
    link = '/anime/'

    def items(self):
        return importing_info.objects.all().order_by("-id")
    def item_name(self, item):
        return item.name

    def item_description(self, item):
        return item.about

    def item_types(self, item):
        return item.types

    def item_gener(self, item):
        return item.gener

    def item_synonyms(self, item):
        return item.synonyms

    def item_premired(self, item):
        return item.premired

    def item_status(self, item):
        return item.status

    def item_link(self, item):
        return reverse('anime_info', kwargs={'id_anime': item.id})
