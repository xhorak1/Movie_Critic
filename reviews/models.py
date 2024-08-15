from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()  # Ensure this field exists

    def __str__(self):
        return self.title
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 11)])
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/10"