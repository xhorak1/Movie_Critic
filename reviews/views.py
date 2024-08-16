from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
def index(request):
    movies = Movie.objects.all()
    return render(request, 'reviews/index.html', {'movies': movies, 'user': request.user})
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
            return redirect('index')  # Redirect to the homepage or another page
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
            return redirect('index')  # Redirect to the homepage or another page
    else:
        form = AuthenticationForm()
    return render(request, 'reviews/login.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()  # Assuming you have a Movie model
    return render(request, 'reviews/movie_list.html', {'movies': movies})