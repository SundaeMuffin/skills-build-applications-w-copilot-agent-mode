from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    TrackerUserViewSet,
    WorkoutViewSet,
    api_root,
)

router = DefaultRouter()
router.register('users', TrackerUserViewSet, basename='users')
router.register('teams', TeamViewSet, basename='teams')
router.register('activities', ActivityViewSet, basename='activities')
router.register('leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register('workouts', WorkoutViewSet, basename='workouts')

urlpatterns = [
    path('', api_root, name='root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
