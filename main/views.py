from django.shortcuts import render, redirect
import urllib.request
import json
from .forms import RegisterForm
from .models import Movie
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    if not Movie.objects.exists():
        url = "https://seleksi-sea-2023.vercel.app/api/movies"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())

        for movie_data in data:
            movie = Movie(
                title=movie_data['title'],
                description=movie_data['description'],
                release_date=movie_data['release_date'],
                poster_url=movie_data['poster_url'],
                age_rating=movie_data['age_rating'],
                ticket_price=movie_data['ticket_price']
            )
            movie.save()

    if request.path == '/home' or request.path == '/' or request.path == '':
        movies = Movie.objects.all()[:5]
        context = {'movies': movies}
        return render(request, 'main/home.html', context)
    elif request.path == "/movies":
        movies = Movie.objects.all()
        context = {'movies': movies}
        return render(request, 'main/movies.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {"form": form})


def account(request):
    if request.user.is_authenticated:
        return render(request, 'registration/account.html')
    else:
        return render(request, 'registration/login.html')


def ticket(request):
    return render(request, 'registration/ticket.html')
