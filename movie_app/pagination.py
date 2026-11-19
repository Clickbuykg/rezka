from rest_framework.pagination import PageNumberPagination

class MoviePagination(PageNumberPagination):
    page_size = 2

class CategoryPagination(PageNumberPagination):
    page_size = 3

class GenrePagination(PageNumberPagination):
    page_size = 4
