from django.contrib import admin
from .models import *

class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name') 

admin.site.register(Actor, ActorAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Director, DirectorAdmin)

class WriterAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Writer, WriterAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','create_date')

admin.site.register(Film, FilmAdmin)


class SerialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','create_date')

admin.site.register(Serial, SerialAdmin)
