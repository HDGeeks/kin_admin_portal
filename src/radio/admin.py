from django.contrib import admin
from .models import *

# Register your models here.
# Radio App
admin.site.register(RadioStationModel)
admin.site.register(FavouritesModel)