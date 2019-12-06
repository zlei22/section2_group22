from django.core.management import BaseCommand
from sightings.models import Sighting
from datetime import datetime
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            sighting = Sighting(
                latitude=item['Y'],
                longitude=item['X'],
                uid=item['Unique Squirrel ID'],
                shift=item['Shift'],
                date=datetime.strptime(item['Date'], '%m%d%Y').date(),
                age='' if item['Age']=='?' else item['Age'],
                color=item['Primary Fur Color'],
                loc=item['Location'],
                specific_loc=item['Specific Location'],
                running=convert(item['Running']),
                chasing=convert(item['Chasing']),
                climbing=convert(item['Climbing']),
                eating=convert(item['Eating']),
                foraging=convert(item['Foraging']),
                other_act=convert(item['Other Activities']),
                kuks=convert(item['Kuks']),
                quaas=convert(item['Quaas']),
                moans=convert(item['Moans']),
                tail_flags=convert(item['Tail flags']),
                tail_twitches=convert(item['Tail twitches']),
                approaches=convert(item['Approaches']),
                indifferent=convert(item['Indifferent']),
                runs_from=convert(item['Runs from']),
            )
            sighting.save()

def convert(string):
    if(string.lower()=='true'):
        return True
    else:
        return False
