from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, TrackerUser, Workout


class ObjectIdToStringSerializerMixin(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(ObjectIdToStringSerializerMixin):
    class Meta:
        model = Team
        fields = ['id', 'name', 'universe', 'captain', 'motto', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TrackerUserSerializer(ObjectIdToStringSerializerMixin):
    class Meta:
        model = TrackerUser
        fields = [
            'id',
            'full_name',
            'hero_name',
            'email',
            'team_name',
            'favorite_activity',
            'points',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ActivitySerializer(ObjectIdToStringSerializerMixin):
    class Meta:
        model = Activity
        fields = [
            'id',
            'user_email',
            'hero_name',
            'activity_type',
            'duration_minutes',
            'calories_burned',
            'completed_at',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LeaderboardEntrySerializer(ObjectIdToStringSerializerMixin):
    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'hero_name', 'team_name', 'points', 'rank', 'streak_days', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class WorkoutSerializer(ObjectIdToStringSerializerMixin):
    class Meta:
        model = Workout
        fields = [
            'id',
            'title',
            'focus_area',
            'difficulty',
            'duration_minutes',
            'assigned_to',
            'instructions',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']