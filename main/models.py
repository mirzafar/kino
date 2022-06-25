from django.db import models

class Actor(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name


class Director(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name


class Writer(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField()
    age_limit = models.IntegerField()
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    writers = models.ManyToManyField(Writer)
    genres = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title


class Serial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField()
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    writers = models.ManyToManyField(Writer)
    genres = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title
