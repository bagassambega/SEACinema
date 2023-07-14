from django.shortcuts import render
import urllib.request
import json
from .forms import RegisterForm
from .models import Movie

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

    movies = Movie.objects.all()

    context = {'movies': movies}

    return render(request, 'main/home.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {"form": form})