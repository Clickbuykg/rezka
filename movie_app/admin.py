from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import UserProfile, Category, Genre, Country, Movie, MovieLanguage, Moment, Rating, Review, director, actor

class GenreInline(admin.TabularInline):
    model = Genre
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [GenreInline]

class MovieLanguageInline(admin.TabularInline):
    model = MovieLanguage
    extra = 1

class MomentInline(admin.TabularInline):
    model = Moment
    extra = 1

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ['movie_name', 'year']
    inlines = [MovieLanguageInline, MomentInline]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(director)
class DirectorAdmin(TranslationAdmin):
    pass

@admin.register(actor)
class ActorAdmin(TranslationAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    pass

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    pass

admin.site.register(Rating)
admin.site.register(Review)
