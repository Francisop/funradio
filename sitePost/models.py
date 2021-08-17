from django.db import models

# Create your models here.

class CollectionsToLookoutFor(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/CollectionsToLookoutFor/")
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class NewMusicTOLookoutFor(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/NewMusicTOLookoutFor/")
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

class NewMusicOnTheBlock(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/NewMusicOnTheBlock/")
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class LatestCollabs(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/LatestCollabs/")
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class AlbumsToLookoutFor(models.Model):
    song_cover = models.ImageField(upload_to = "siteImages/AlbumsToLookoutFor/")
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=300)
    audio = models.FileField(upload_to="songs/")
       
    def __str__(self):
        return self.artist +" - " + self.song_title
