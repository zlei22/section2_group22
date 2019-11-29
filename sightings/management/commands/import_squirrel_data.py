import csv
from django.core.management import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Load a csv file into the database'
    
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)


    def handle(self, *args, **kwargs):
        path = args[0]
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                squirrel = Squirrel.objects.create(
                    longitude=row[0],
                    latitude=row[1],
                    uid=row[2],
                    shift=row[4],
                    date=row[5],
                    age=row[7],
                    color=row[8],
                    loc=row[12],
                    specific_loc=row[14],
                    running=row[15],
                    chasing=row[16],
                    climbing=row[17],
                    eating=row[18],
                    foraging=row[19],
                    other_act=row[20],
                    kuks=row[21],
                    quaas=row[22],
                    moans=row[23],
                    tail_flags=row[24],
                    tail_twitches=row[25],
                    approaches=row[26],
                    indifferent=row[27],
                    runs_from=row[28],
                )
