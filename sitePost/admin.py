from django.contrib import admin
from sitePost.models import (AlbumsToLookoutFor,CollectionsToLookoutFor,LatestCollabs,NewMusicOnTheBlock,NewMusicTOLookoutFor,Song)

# Register your models here.
admin.site.register(AlbumsToLookoutFor)
admin.site.register(CollectionsToLookoutFor)
admin.site.register(LatestCollabs)
admin.site.register(NewMusicOnTheBlock)
admin.site.register(NewMusicTOLookoutFor)
admin.site.register(Song)