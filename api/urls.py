from django.urls import path, include
from rest_framework import routers
from .views import OurTeamViewSet, UserViewSet, TeamPageViewSet, NavbarViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('our_team', OurTeamViewSet)
router.register('team_page', TeamPageViewSet)
router.register('navbar', NavbarViewSet)
router.register('photo', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]