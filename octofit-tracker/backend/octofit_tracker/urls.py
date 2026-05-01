import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    TrackerUserViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()
router.register('users', TrackerUserViewSet, basename='users')
router.register('teams', TeamViewSet, basename='teams')
router.register('activities', ActivityViewSet, basename='activities')
router.register('leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register('workouts', WorkoutViewSet, basename='workouts')

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = 'http://localhost:8000'


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'users': f'{base_url}/api/users/',
            'teams': f'{base_url}/api/teams/',
            'activities': f'{base_url}/api/activities/',
            'leaderboard': f'{base_url}/api/leaderboard/',
            'workouts': f'{base_url}/api/workouts/',
        }
    )

urlpatterns = [
    path('', api_root, name='root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
