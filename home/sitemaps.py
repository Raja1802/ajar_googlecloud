from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.urls import reverse
from django.apps import apps
importing_info = apps.get_model('info', 'Anime')
importing_episode = apps.get_model('play', 'Episode')


class EpisodeSitemap_1(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        return importing_episode.objects.order_by('-id')[:20000]
    
    
class EpisodeSitemap_2(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        return importing_episode.objects.order_by('-id')[20001:40000]
    
    
class EpisodeSitemap_3(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        return importing_episode.objects.order_by('-id')[40001:80000]
    
class InfoSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    

    def items(self):
        return importing_info.objects.order_by('-id')
