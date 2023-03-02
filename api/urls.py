from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register("artists", views.ArtistsViewSet, basename="artists")
router.register("albums", views.AlbumsSongsViewSet, basename="albums")
router.register("artists-albums", views.ArtistsAlbumsViewSet, basename="artist-albums")
router.register(
    "albums-enriched", views.AlbumsEnrichedViewSet, basename="albums-enriched"
)
urlpatterns = router.urls
