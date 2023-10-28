from django.shortcuts import render
from django.views import View
from .models import Movie, Director, Genre
from django.http import JsonResponse

def index(request):
    movies = Movie.objects.all()
    directors = Director.objects.all()

    return render(
        request,
        'index.html',
        context={
            'title': 'Movies and Directors',
            'num_movies': movies.count(),
            'movies': movies,
            'num_directors': directors.count(),
            'directors': directors,
        }
    )
class director(View):
    def director(request, director):
        directorExists = list(filter(lambda dir: str(dir.lastName) + " " + str(dir.firstName) == director, Director.objects.all()))
        if len(directorExists) != 0:
            num_movies = list(filter(lambda movi: str(movi.director) == director, Movie.objects.all()))
            return render(
                request,
                'director.html',
                context={
                    'title': directorExists[0].firstName + " " + directorExists[0].lastName,
                    'num_movies': len(num_movies),
                    'movies': num_movies, #recorrer este objeto en la plantilla par amostrar toda la info de cada pelicula
                }
            )
        else:
            return render(
                request,
                'notFound.html',
                context={
                    'title': 'Error: Director not found'
                }
            )

#Test de peticion get, esta parte es ajena al ejercicio original
class getDirectors(View):
    def get(self, request):
        directors = Director.objects.all()
        return JsonResponse(list(directors.values()), safe=False)

class form (View):
    def form(request):
        return render(
            request,
            'form.html',
        )

class requestForm(View):
    def requestForm(request):
        text = request.POST["message"]
        return render(
            request,
            'requestForm.html',
            context={
                'title': 'requestForm',
                'message': text,
            }
        )