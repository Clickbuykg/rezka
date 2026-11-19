from random import choice

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

STATUS_CHOICES = (
    ('simple', 'simple'),
    ('pro', 'pro'),
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(100)],
                                           null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_image', null=True, blank=True)
    user_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')
    data_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name



class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name



class director(models.Model):
    director_name = models.CharField(max_length=43)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)],
                                           null=True, blank=True)
    director_image = models.ImageField(upload_to='photo_director', null=True, blank=True)

    def __str__(self):
        return self.director_name


class actor(models.Model):
    actor_name = models.CharField(max_length=43)
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)],
                                           null=True, blank=True)
    actor_image = models.ImageField(upload_to='photo_actor', null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre_name = models.CharField(max_length=43)


    def __str__(self):
        return self.genre_name



class Movie(models.Model):
    TYPES_CHOICES = (
    ('144p', '144p'),
    ('360p', '360p'),
    ('720p', '720p'),
    ('1080p', '1080p'),
    )
    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    slogan = models.CharField(max_length=100)
    country = models.ManyToManyField(Country, related_name='country_movies')
    director = models.ManyToManyField(director, related_name='director_movies')
    actor = models.ManyToManyField(actor, related_name='actor_movies')
    genre = models.ManyToManyField(Genre, related_name='genre_movies')
    types = models.CharField(max_length=10, choices=[('144p', '144p'), ('360p', '360p'), ('720p', '720p'), ('1080p', '1080p')], default='720p')
    movie_time = models.PositiveSmallIntegerField()
    movie_trailer = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    movie_image = models.ImageField(upload_to='movie_photo', null=True, blank=True)
    status_movie = models.CharField(max_length=64, choices=STATUS_CHOICES)


    def __str__(self):
        return self.movie_name



class MovieLanguage(models.Model):
    language = models.CharField(max_length=43)
    video = models.FileField(upload_to='movie_language')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return self.language


class Moment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moment = models.ImageField(upload_to='movie_moment',
                                     null=True, blank=True)


    def __str__(self):
        return f'{self.movie.movie_name}'


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 11)],
                                            null=True, blank=True)


    def __str__(self):
        return f'{self.movie.movie_name}'



class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.movie_name}'


class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.review.movie.movie_name}'



class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'



class FavoriteItem(models.Model):
    Favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.movie.movie_name}'



class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    view_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}'

