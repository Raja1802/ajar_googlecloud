from django.contrib.sitemaps import Sitemap
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
importing_episode = apps.get_model('play', 'Episode')


class TodoSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        urls = {
           'i' = importing_episode.objects.all()[:10]
        }
        return urls
