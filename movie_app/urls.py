from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, CustomLoginView, LogoutView,
    UserProfileViewSet, MovieLanguageViewSet,
    MomentViewSet, RatingViewSet, ReviewViewSet,
    FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet,
    MovieListAPIView, MovieDetailAPIView,
    CategoryListAPIView, CategoryDetailAPIView,
    CountryListAPIView, CountryDetailAPIView,
    DirectorListAPIView, DirectorDetailAPIView,
    ActorListAPIView, ActorDetailAPIView,
    GenreListAPIView, GenreDetailAPIView
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user')
router.register(r'movie_language', MovieLanguageViewSet, basename='movie_language')
router.register(r'moment', MomentViewSet, basename='moment')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'favorite_item', FavoriteMovieViewSet, basename='favorite_item')
router.register(r'history', HistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
]
