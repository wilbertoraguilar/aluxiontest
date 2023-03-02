from api.models import Artists, Albums, Tracks
from rest_framework import serializers


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ["id", "name"]


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = ["name"]


class AlbumTracksSerializer(serializers.ModelSerializer):
    tracks = TracksSerializer(many=True, read_only=True)

    class Meta:
        model = Albums
        fields = ["id", "title", "tracks"]


class AlbumEnrichedSerializer(serializers.ModelSerializer):
    total_tracks = serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Albums
        fields = ["id", "title", "artist_name", "total_tracks"]

    def get_total_tracks(self, album):
        return album.tracks.count()

    def get_artist_name(self, album):
        return album.artist.name


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ["title"]


class ArtistAlbumsSerializer(serializers.ModelSerializer):
    albums = AlbumsSerializer(many=True, read_only=True)

    class Meta:
        model = Artists
        fields = ["id", "name", "albums"]

