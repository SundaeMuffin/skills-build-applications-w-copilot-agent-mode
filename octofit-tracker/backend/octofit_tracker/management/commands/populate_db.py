from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from octofit_tracker.models import Activity, LeaderboardEntry, Team, TrackerUser, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Resetting OctoFit collections...')
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        TrackerUser.objects.all().delete()
        Team.objects.all().delete()

        teams = [
            {
                'name': 'Team Marvel',
                'universe': 'Marvel',
                'captain': 'Captain Marvel',
                'motto': 'Higher, further, faster.',
            },
            {
                'name': 'Team DC',
                'universe': 'DC',
                'captain': 'Wonder Woman',
                'motto': 'Truth, justice, and teamwork.',
            },
        ]
        for payload in teams:
            Team.objects.create(**payload)

        users = [
            {
                'full_name': 'Peter Parker',
                'hero_name': 'Spider-Man',
                'email': 'spiderman@octofit.dev',
                'team_name': 'Team Marvel',
                'favorite_activity': 'Wall climbs',
                'points': 98,
            },
            {
                'full_name': 'Carol Danvers',
                'hero_name': 'Captain Marvel',
                'email': 'captainmarvel@octofit.dev',
                'team_name': 'Team Marvel',
                'favorite_activity': 'Flight intervals',
                'points': 110,
            },
            {
                'full_name': 'Bruce Wayne',
                'hero_name': 'Batman',
                'email': 'batman@octofit.dev',
                'team_name': 'Team DC',
                'favorite_activity': 'Night sprints',
                'points': 102,
            },
            {
                'full_name': 'Diana Prince',
                'hero_name': 'Wonder Woman',
                'email': 'wonderwoman@octofit.dev',
                'team_name': 'Team DC',
                'favorite_activity': 'Strength circuits',
                'points': 108,
            },
        ]
        for payload in users:
            TrackerUser.objects.create(**payload)

        now = timezone.now()
        activities = [
            {
                'user_email': 'spiderman@octofit.dev',
                'hero_name': 'Spider-Man',
                'activity_type': 'Parkour run',
                'duration_minutes': 45,
                'calories_burned': 520,
                'completed_at': now - timedelta(days=1),
                'notes': 'Focused on rooftop intervals.',
            },
            {
                'user_email': 'captainmarvel@octofit.dev',
                'hero_name': 'Captain Marvel',
                'activity_type': 'HIIT flight drill',
                'duration_minutes': 35,
                'calories_burned': 480,
                'completed_at': now - timedelta(days=2),
                'notes': 'High altitude conditioning.',
            },
            {
                'user_email': 'batman@octofit.dev',
                'hero_name': 'Batman',
                'activity_type': 'Night sprint session',
                'duration_minutes': 40,
                'calories_burned': 450,
                'completed_at': now - timedelta(days=1, hours=5),
                'notes': 'Stair climbs in full gear.',
            },
            {
                'user_email': 'wonderwoman@octofit.dev',
                'hero_name': 'Wonder Woman',
                'activity_type': 'Strength circuit',
                'duration_minutes': 50,
                'calories_burned': 610,
                'completed_at': now - timedelta(hours=12),
                'notes': 'Lasso core finisher.',
            },
        ]
        for payload in activities:
            Activity.objects.create(**payload)

        leaderboard = [
            {'hero_name': 'Captain Marvel', 'team_name': 'Team Marvel', 'points': 110, 'rank': 1, 'streak_days': 9},
            {'hero_name': 'Wonder Woman', 'team_name': 'Team DC', 'points': 108, 'rank': 2, 'streak_days': 8},
            {'hero_name': 'Batman', 'team_name': 'Team DC', 'points': 102, 'rank': 3, 'streak_days': 6},
            {'hero_name': 'Spider-Man', 'team_name': 'Team Marvel', 'points': 98, 'rank': 4, 'streak_days': 7},
        ]
        for payload in leaderboard:
            LeaderboardEntry.objects.create(**payload)

        workouts = [
            {
                'title': 'Spider Agility Ladder',
                'focus_area': 'Agility',
                'difficulty': 'Medium',
                'duration_minutes': 25,
                'assigned_to': 'Spider-Man',
                'instructions': 'Alternate ladder drills with jump squats for five rounds.',
            },
            {
                'title': 'Marvel Core Blast',
                'focus_area': 'Core',
                'difficulty': 'Hard',
                'duration_minutes': 30,
                'assigned_to': 'Captain Marvel',
                'instructions': 'Complete plank holds, hollow rocks, and medicine ball throws.',
            },
            {
                'title': 'Gotham Sprint Pyramid',
                'focus_area': 'Cardio',
                'difficulty': 'Hard',
                'duration_minutes': 28,
                'assigned_to': 'Batman',
                'instructions': 'Run sprint intervals of 100m, 200m, 300m, then back down.',
            },
            {
                'title': 'Amazon Strength Flow',
                'focus_area': 'Strength',
                'difficulty': 'Medium',
                'duration_minutes': 32,
                'assigned_to': 'Wonder Woman',
                'instructions': 'Cycle through lunges, presses, and farmer carries for six rounds.',
            },
        ]
        for payload in workouts:
            Workout.objects.create(**payload)

        self.stdout.write(self.style.SUCCESS('OctoFit test data loaded successfully.'))