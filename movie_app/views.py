from rest_framework import viewsets, generics, filters, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    UserProfile, Category, Genre, Country, Movie, MovieLanguage,
    Moment, Rating, Review, director, actor, Favorite, FavoriteItem, History
)
from .serializers import (
    UserProfileSerializer, CategorySerializer,
    CountryListSerializer, CountryDetailSerializer,
    DirectorListSerializer, DirectorDetailSerializer,
    ActorListSerializer, ActorDetailSerializer,
    GenreListSerializer, GenreDetailSerializer,
    MovieListSerializer, MovieDetailSerializer, MovieLanguageSerializer,
    MomentSerializer, RatingSerializer, ReviewSerializer,
    FavoriteSerializer, FavoriteMovieSerializer, HistorySerializer
)
from .pagination import MoviePagination, CategoryPagination, GenrePagination
from .permissions import CheckStatus, CheckOwner


class RegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if 'password' in request.data:
            user.set_password(request.data['password'])
            user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]


class MovieLanguageViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguage.objects.all()
    serializer_class = MovieLanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MomentViewSet(viewsets.ModelViewSet):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['country', 'genre', 'status_movie', 'actor']
    search_fields = ['movie_name']
    ordering_fields = ['year']
    pagination_class = MoviePagination
    permission_classes = [permissions.AllowAny]


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CheckStatus]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class DirectorListAPIView(generics.ListAPIView):
    queryset = director.objects.all()
    serializer_class = DirectorListSerializer


class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = director.objects.all()
    serializer_class = DirectorDetailSerializer


class ActorListAPIView(generics.ListAPIView):
    queryset = actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = actor.objects.all()
    serializer_class = ActorDetailSerializer


class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    pagination_class = GenrePagination


class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer
