import csv
from django.core.management import BaseCommand
from sightings.models import Sighting
from datetime import datetime

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('data_path')

    def handle(self,*args,**kwargs):
        path=kwargs['data_path']
        c = 0
        with open(path, 'rt') as f:
            reader = csv.DictReader(f,fieldnames=('X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat Long','Zip Codes','Community Districts','Borough Boundaries','City Council Districts',  'Police Precincts') )
            headers =next(reader)
                
            for row in reader:
                sightings = Sighting.objects.create(
                    uid=row['Unique Squirrel ID'],
                    longitude=row['X'],
                    latitude=row['Y'],
                    shift=row['Shift'],
                    date=datetime.strptime(row['Date'], '%m%d%Y').date(),
                    age=row['Age'],
                    color=row['Primary Fur Color'],
                    loc=row['Location'],
                    specific_loc=row['Specific Location'],
                    running=convert(row['Running']),
                    chasing=convert(row['Chasing']),
                    climbing=convert(row['Climbing']),
                    eating=convert(row['Eating']),
                    foraging=convert(row['Foraging']),
                    other_act=convert(row['Other Activities']),
                    kuks=convert(row['Kuks']),
                    quaas=convert(row['Quaas']),
                    moans=convert(row['Moans']),
                    tail_flags=convert(row['Tail flags']),
                    tail_twitches=convert(row['Tail twitches']),
                    approaches=convert(row['Approaches']),
                    indifferent=convert(row['Indifferent']),
                    runs_from=convert(row['Runs from']),
                    )
                c=c+1
        self.stdout.write("File path: %s" % path)
        self.stdout.write("Rows inserted: %s " % c)
    
def convert(string):
    if(string.lower()=='true'):
        return True
    else:
        return False
