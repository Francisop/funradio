from django.contrib import admin
from sitePost.models import (CollectionsToLookoutFor, LatestAlbums, EventsInTheCity, NewMusicOnTheBlock,Song)

# Register your models here.
admin.site.register(LatestAlbums)
admin.site.register(EventsInTheCity)
admin.site.register(NewMusicOnTheBlock)
admin.site.register(Song)