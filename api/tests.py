from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Artists, Albums, Tracks, Genres, MediaTypes
import pdb


class ArtistsViewSetTestCase(APITestCase):
    def test_artists(self):
        artist = Artists(name="testartist")
        artist.save()
        url = reverse("artists-list")
        response = self.client.get(url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class AlbumsSongsViewSetTestCase(APITestCase):
    def test_albums(self):
        artist = Artists(name="testartist")
        artist.save()
        album = Albums(title="Album1", artist=artist)
        album.save()
        genre = Genres(name="Rock")
        genre.save()
        media_type = MediaTypes(name="Tape")
        media_type.save()
        track = Tracks(
            name="Track1",
            album=album,
            milliseconds=50,
            bytes=50,
            unitPrice=50,
            genre=genre,
            mediaType=media_type,
        )
        track.save()
        url = reverse("albums-list")
        response = self.client.get(url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]["tracks"]), 1)


class ArtistsAlbumsViewSetTestCase(APITestCase):
    def test_artists_albums(self):
        artist = Artists(name="testartist")
        artist.save()
        album = Albums(title="Album1", artist=artist)
        album.save()
        url = reverse("artist-albums-list")
        response = self.client.get(url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]["albums"]), 1)


class AlbumsEnrichedViewSetTestCase(APITestCase):
    def test_albums_enriched(self):
        artist = Artists(name="testartist")
        artist.save()
        album = Albums(title="Album1", artist=artist)
        album.save()
        genre = Genres(name="Rock")
        genre.save()
        media_type = MediaTypes(name="Tape")
        media_type.save()
        track = Tracks(
            name="Track1",
            album=album,
            milliseconds=50,
            bytes=50,
            unitPrice=50,
            genre=genre,
            mediaType=media_type,
        )
        track.save()
        url = reverse("albums-enriched-list")
        response = self.client.get(url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["total_tracks"], 1)