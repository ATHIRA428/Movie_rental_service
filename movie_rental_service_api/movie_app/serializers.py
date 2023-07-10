from django.utils import timezone
from rest_framework import serializers
from .models import Movie

def validate_movie_title(title):
    if not title.startswith('Movie-'):
        raise serializers.ValidationError('The title must start with "Movie-".')
    if len(title) < 2:
        raise serializers.ValidationError('The title must have a minimum of 2 characters.')
    if len(title) > 100:
        raise serializers.ValidationError('The title can have a maximum of 100 characters.')
    return title

def validate_movie_release_date(release_date):
    if release_date > timezone.now().date():
        raise serializers.ValidationError('The release date cannot be in the future.')
    if release_date < timezone.now().date() - timezone.timedelta(days=30 * 365):
        raise serializers.ValidationError('The release date must be within the last 30 years.')
    return release_date

def validate_movie_duration_minutes(duration_minutes):
    if duration_minutes < 1:
        raise serializers.ValidationError('The duration must be at least 1 minute.')
    if duration_minutes > 600:
        raise serializers.ValidationError('The duration cannot exceed 600 minutes (10 hours).')
    return duration_minutes

def validate_movie_genre(genre):
    valid_choices = ["Action", "Drama", "Comedy", "Thriller", "Sci-Fi"]
    if genre not in valid_choices:
        raise serializers.ValidationError('Invalid genre choice.')
    return genre

def validate_movie_rating(rating):
    if rating is not None and (rating < 0.0 or rating > 10.0):
        raise serializers.ValidationError('The rating must be between 0.0 and 10.0.')
    return rating

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True,
        min_length=2,
        max_length=100,
        validators=[validate_movie_title],
        error_messages={
            'required': 'The title field is required.',
        }
    )
    release_date = serializers.DateField(
        required=True,
        validators=[validate_movie_release_date],
        error_messages={
            'required': 'The release date field is required.',
        }
    )
    genre = serializers.CharField(
        required=True,
        validators=[validate_movie_genre],
        error_messages={
            'required': 'The genre field is required.',
        }
    )
    duration_minutes = serializers.IntegerField(
        required=True,
        validators=[validate_movie_duration_minutes],
        error_messages={
            'required': 'The duration minutes field is required.',
        }
    )
    rating = serializers.FloatField(
        required=False,
        validators=[validate_movie_rating],
        error_messages={
            'invalid': 'Invalid rating value.',
        }
    )

    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'genre', 'duration_minutes', 'rating']
