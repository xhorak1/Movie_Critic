from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MovieForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


def index(request):
    query = request.GET.get('query', '')
    if query:
        search_results = Movie.objects.filter(title__icontains=query)
    else:
        search_results = None

    movies = Movie.objects.all()

    return render(request, 'reviews/index.html', {
        'movies': movies,
        'search_results': search_results,
    })
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            review_text = request.POST.get('review_text')
            rating = request.POST.get('rating')
            Review.objects.create(movie=movie, user=request.user, review_text=review_text, rating=rating)
            return redirect('movie_detail', movie_id=movie_id)
        else:
            return redirect('login')  # Redirect to login if the user is not authenticated

    return render(request, 'reviews/movie_detail.html', {'movie': movie, 'reviews': reviews})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Sign up successful.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'reviews/signup.html', {'form': form})

def submit_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form, 'movie': movie})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('index')  # Redirect to the homepage or another page
    else:
        form = AuthenticationForm()
    return render(request, 'reviews/login.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()  # Assuming you have a Movie model
    return render(request, 'reviews/movie_list.html', {'movies': movies})

def movie_database(request):
    genre = request.GET.get('genre', '')
    sort_by = request.GET.get('sort', 'title')

    if genre:
        movies = Movie.objects.filter(genre__iexact=genre)
    else:
        movies = Movie.objects.all()

    movies = movies.order_by(sort_by)
    genres = Movie.objects.values_list('genre', flat=True).distinct()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            # Check if a movie with the same title exists
            title = form.cleaned_data.get('title')
            if Movie.objects.filter(title__iexact=title).exists():
                form.add_error('title', 'Dear user, a movie with this title already exists in the database.')
            else:
                form.save()
                messages.success(request, 'Movie added successfully.')
                return redirect('movie_database')
        else:
            # If form is not valid, messages will automatically be handled in the template
            messages.error(request, 'Please correct the errors below.')

    else:
        form = MovieForm()

    return render(request, 'reviews/movie_database.html', {
        'movies': movies,
        'genres': genres,
        'form': form,
    })

def about_movie_critic(request):
    return render(request, 'reviews/about_movie_critic.html')

def privacy_policy(request):
    return render(request, 'reviews/privacy_policy.html')

def custom_logout(request):
    logout(request)
    return redirect('index')

