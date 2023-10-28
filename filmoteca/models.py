from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Descripcion de la pelicula")
    yearPremiere = models.DateField(null=True, blank=True) #Anno de estreno
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

class Director(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    dateOfBirth = models.DateField(null=True, blank=True)
    dateOfDeath = models.DateField("Dead", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.lastName, self.firstName)