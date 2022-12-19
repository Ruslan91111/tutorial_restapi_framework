from rest_framework.viewsets import ModelViewSet

from movies.models import Movies
from movies.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer









