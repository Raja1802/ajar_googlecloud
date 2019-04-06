from django.contrib.sitemaps import Sitemap
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
importing_episode = apps.get_model('play', 'Episode')


class TodoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return importing_episode.objects.all()
