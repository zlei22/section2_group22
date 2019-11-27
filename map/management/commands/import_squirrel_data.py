from map.models import Squirrels

import csv
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('positionArg')

    def handle(self,*args,**kargs):
        path=kargs['positionArg']
        with open(path, 'rt') as f:
            reader = csv.DictReader(f, dialect='excel')
            for row in reader:
                Squirrels.objects.create(
                    Unique_Squirrel_ID=['Unique_Squirrel_ID'],
                    Longitude=row['x'],
                    Latitude=row['y']
                    )
