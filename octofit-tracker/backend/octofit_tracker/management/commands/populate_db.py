from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data safely

        # Use pymongo to drop collections directly
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        for coll in ['users', 'teams', 'activities', 'workouts', 'leaderboard']:
            db.drop_collection(coll)

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date=timezone.now())
        Activity.objects.create(user=captain, type='Cycling', duration=45, calories=400, date=timezone.now())
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500, date=timezone.now())
        Activity.objects.create(user=superman, type='Flying', duration=120, calories=1000, date=timezone.now())

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Sidekick Cardio', description='Cardio for sidekicks', difficulty='Medium')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700, rank=1)
        Leaderboard.objects.create(team=dc, points=1500, rank=1)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
