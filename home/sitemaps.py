from django.contrib.sitemaps import Sitemap
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
importing_episode = apps.get_model('play', 'Episode')


class EpisodeSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        return importing_episode.objects.all()[:10]
    
class InfoSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        return importing_info.objects.all()[:10]  
