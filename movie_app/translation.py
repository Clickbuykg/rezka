from modeltranslation.translator import register, TranslationOptions
from .models import Category, Genre, Country, Movie, MovieLanguage, director, actor

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(MovieLanguage)
class MovieLanguageTranslationOptions(TranslationOptions):
    fields = ('language',)


@register(director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio')

@register(actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name',)
