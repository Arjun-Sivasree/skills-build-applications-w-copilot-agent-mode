from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=30)
        self.assertEqual(str(activity), 'testuser - run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='testuser', score=100)
        self.assertEqual(str(lb), 'testuser: 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(str(workout), 'Pushups')
