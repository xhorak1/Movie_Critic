from django.db import models
from django.contrib.auth.models import User
from datetime import date

def get_default_release_date():
    return date(1900, 1, 1)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.title
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.movie.title}"