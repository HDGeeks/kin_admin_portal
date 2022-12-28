from django.contrib import admin
from .models import *

# Register your models here.
# Music App
@admin.register(ArtistsModel)
class ArtistsModelAdmin(admin.ModelAdmin):
    list_display = (
            # 'id', 
            'artist_name', 
            'artist_title', 
            'artist_status',
            'artist_releaseDate',
            'artist_description',
            'artist_viewcount',
            # 'artist_profileImage',
            'artist_FUI',
            'created_at',
            'updated_at'
        )

@admin.register(AlbumsModel)
class AlbumsModelAdmin(admin.ModelAdmin):
    list_display = (
            # 'id',
            'album_name',
            'album_rating',
            'album_status',
            'album_releaseDate',
            'album_description',
            'album_viewcount',
            # 'album_coverImage',
            'album_price',
            'created_at',
            'updated_at'
        )
    # pass

@admin.register(GenresModel)
class GenresModelAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'genre_name',
        'genre_rating',
        'genre_status',
        'genre_description',
        'genre_viewcount',
        # 'genre_coverImage',
        'created_at',
        'updated_at'
    )

@admin.register(TracksModel)
class TracksModelAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'track_name',
        'track_rating',
        'track_status',
        'track_releaseDate',
        'track_description',
        'track_viewcount',
        # 'track_coverImage',
        'track_audioFile',
    )

@admin.register(PlayListsModel)
class PlayListsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PlayListTracksModel)
class PlayListTracksModelAdmin(admin.ModelAdmin):
    pass

@admin.register(FavouritesModel)
class FavouritesModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PurchasedTracksModel)
class PurchasedTracksModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PurchasedAlbumsModel)
class PurchasedAlbumsModelAdmin(admin.ModelAdmin):
    pass