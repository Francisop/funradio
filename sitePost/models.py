from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.

    
class NewMusicOnTheBlock(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/NewMusicOnTheBlock/")
    title = models.CharField(max_length=200)
    
    
    objects = models.Manager()
    
    def __str__(self):
        return self.title


class EventsInTheCity(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/LatestCollabs/")
    title = models.CharField(max_length=200)
    
    objects = models.Manager()
    
    def __str__(self):
        return self.title


class LatestAlbums(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/AlbumsToLookoutFor/")
    title = models.CharField(max_length=200)
    
    objects = models.Manager()
    
    def __str__(self):
        return self.title
    
    
    
    
class SongManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0,count - 1)
        return self.all()[random_index]
    
    
    
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=300)
    audio = models.FileField(upload_to="songs/")
    artist_image = models.ImageField(upload_to = "siteImages/song-image/")
    artist_desc = models.CharField(max_length=600)
    
    objects = models.Manager()
    randomise = SongManager()
       
    def __str__(self):
        return self.artist +" - " + self.song_title




