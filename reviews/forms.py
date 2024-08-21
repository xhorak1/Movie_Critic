from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'genre', 'rating', 'release_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Movie.objects.filter(title=title).exists():
            raise forms.ValidationError("A movie with this title already exists in the database.")
        return title
