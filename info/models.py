from django.db import models
from django.contrib.sitemaps import ping_google
from django.urls import reverse

class Anime(models.Model):
    class Meta:
        db_table = 'info'
    cover = models.CharField(max_length=200, null=True, blank=True)
    tags = models.CharField(max_length=600, null=True, blank=True)
    studios = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    durination = models.CharField(max_length=15, null=True, blank=True)
    scores = models.CharField(max_length=20, null=True, blank=True)
    aired = models.CharField(max_length=30, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    gener = models.CharField(max_length=200, null=True, blank=True)
    quality = models.CharField(max_length=10, null=True, blank=True)
    synonyms = models.CharField(max_length=300, null=True, blank=True)
    premired = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    types = models.CharField(max_length=15, null=True, blank=True)


    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    
    def get_absolute_url(self):
            return reverse('anime_info', kwargs={'id_anime': self.id})
        
   
    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

