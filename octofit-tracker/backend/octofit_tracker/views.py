import os

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Activity, LeaderboardEntry, Team, TrackerUser, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    TrackerUserSerializer,
    WorkoutSerializer,
)

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


class TrackerUserViewSet(viewsets.ModelViewSet):
    queryset = TrackerUser.objects.all().order_by('hero_name')
    serializer_class = TrackerUserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-completed_at')
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('rank', '-points')
    serializer_class = LeaderboardEntrySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by('title')
    serializer_class = WorkoutSerializer