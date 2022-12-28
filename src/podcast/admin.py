from django.contrib import admin
from .models import *

# Register your models here.
# Podcast App
admin.site.register(PodcastsModel)
admin.site.register(SeasonsModel)
admin.site.register(CategoriesModel)
admin.site.register(EpisodesModel)