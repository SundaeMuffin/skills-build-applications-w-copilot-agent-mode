from djongo import models


class TimestampedDocument(models.Model):
    _id = models.ObjectIdField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(TimestampedDocument):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=50)
    captain = models.CharField(max_length=100)
    motto = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'teams'
        ordering = ['name']

    def __str__(self):
        return self.name


class TrackerUser(TimestampedDocument):
    full_name = models.CharField(max_length=120)
    hero_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100)
    favorite_activity = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'users'
        ordering = ['hero_name']

    def __str__(self):
        return self.hero_name


class Activity(TimestampedDocument):
    user_email = models.EmailField()
    hero_name = models.CharField(max_length=120)
    activity_type = models.CharField(max_length=80)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    completed_at = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-completed_at']

    def __str__(self):
        return f'{self.hero_name}: {self.activity_type}'


class LeaderboardEntry(TimestampedDocument):
    hero_name = models.CharField(max_length=120)
    team_name = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    streak_days = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank', '-points']

    def __str__(self):
        return f'{self.rank}. {self.hero_name}'


class Workout(TimestampedDocument):
    title = models.CharField(max_length=120)
    focus_area = models.CharField(max_length=120)
    difficulty = models.CharField(max_length=40)
    duration_minutes = models.PositiveIntegerField()
    assigned_to = models.CharField(max_length=120)
    instructions = models.TextField()

    class Meta:
        db_table = 'workouts'
        ordering = ['title']

    def __str__(self):
        return self.title