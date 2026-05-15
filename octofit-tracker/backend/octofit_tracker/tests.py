from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, calories=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=123)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_user(self):
        self.assertEqual(self.activity.user.email, 'test@example.com')

    def test_leaderboard_user(self):
        self.assertEqual(self.leaderboard.user.name, 'Test User')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')
