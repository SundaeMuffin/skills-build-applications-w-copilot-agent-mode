from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, TrackerUser, Workout

admin.site.register(TrackerUser)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(LeaderboardEntry)
admin.site.register(Workout)