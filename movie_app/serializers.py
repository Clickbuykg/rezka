from rest_framework import serializers
from .models import (
    UserProfile, Category, Genre, Country, Movie, MovieLanguage,
    Moment, Rating, Review, director, actor, Favorite, FavoriteItem, History
)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MovieLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguage
        fields = '__all__'


class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'genre', 'movie_image', 'status_movie']


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']


class CountryDetailSerializer(serializers.ModelSerializer):
    country_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'country_movies']


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = director
        fields = ['id', 'director_name']


class DirectorDetailSerializer(serializers.ModelSerializer):
    director_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = director
        fields = ['director_name', 'bio', 'director_image', 'director_movies']


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = ['id', 'actor_name']


class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = actor
        fields = ['actor_name', 'age', 'actor_image', 'actor_movies']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']


class GenreDetailSerializer(serializers.ModelSerializer):
    genre_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name', 'genre_movies']


class MovieDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreListSerializer(many=True, read_only=True)
    country = CountryListSerializer(many=True, read_only=True)
    director = DirectorListSerializer(many=True, read_only=True)
    actor = ActorListSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id', 'movie_name', 'year', 'slogan', 'category', 'genre', 'country',
            'director', 'actor', 'types', 'movie_time', 'movie_trailer',
            'description', 'movie_image', 'status_movie', 'ratings', 'reviews', 'average_rating'
        ]

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            total = 0
            for r in ratings:
                val = getattr(r, 'stars', getattr(r, 'rating', 0))
                if val:
                    total += int(val)
            return total / ratings.count()
        return 0


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
