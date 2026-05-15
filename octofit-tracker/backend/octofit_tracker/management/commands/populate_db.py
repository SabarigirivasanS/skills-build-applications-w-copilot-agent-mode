from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data in order to avoid FK issues and Djongo unhashable errors
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        for user in User.objects.all():
            if user.pk:
                user.delete()
        for team in Team.objects.all():
            if team.pk:
                team.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        Activity.objects.create(user=clark, type='Yoga', duration=20, calories=100)

        # Create Workouts
        Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel heroes')
        Workout.objects.create(name='Justice League Strength', description='Strength training for DC heroes')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=1000)
        Leaderboard.objects.create(user=steve, score=900)
        Leaderboard.objects.create(user=bruce, score=950)
        Leaderboard.objects.create(user=clark, score=980)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
