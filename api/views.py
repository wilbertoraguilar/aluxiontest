from api.models import Artists, Albums
from rest_framework import status, viewsets
from api import serializers


class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = serializers.ArtistsSerializer


class AlbumsSongsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = serializers.AlbumTracksSerializer


class ArtistsAlbumsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = serializers.ArtistAlbumsSerializer


class AlbumsEnrichedViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = serializers.AlbumEnrichedSerializer
