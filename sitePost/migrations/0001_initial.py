# Generated by Django 3.2.6 on 2021-08-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumsToLookoutFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_cover', models.ImageField(upload_to='siteImages/AlbumsToLookoutFor/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionsToLookoutFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_cover', models.ImageField(upload_to='siteImages/CollectionsToLookoutFor/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LatestCollabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_cover', models.ImageField(upload_to='siteImages/LatestCollabs/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NewMusicOnTheBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_cover', models.ImageField(upload_to='siteImages/NewMusicOnTheBlock/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NewMusicTOLookoutFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_cover', models.ImageField(upload_to='siteImages/NewMusicTOLookoutFor/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=300)),
                ('audio', models.FileField(upload_to='songs/')),
            ],
        ),
    ]
