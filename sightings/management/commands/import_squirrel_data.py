from sightings.models import Sightings

import csv
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('data_path',type='str',help ='The data path to import')

    def handle(self,*args,**kwargs):
        path=kwargs['data_path']
        c = 0
        with open(path, 'rt') as f:
            reader = csv.DictReader(f,fieldnames=('X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat Long','Zip Codes','Community Districts','Borough Boundaries','City Council Districts',  'Police Precincts') )
            headers =next(reader)
                
            for row in reader:
                Sightings.objects.create(
                    uid=row['Unique_Squirrel_ID'],
                    longitude=row['X'],
                    latitude=row['Y'],
                    shift =row['Shift'],
                    date= datetime.strptime(row['Date'], '%m%d%Y').date()
                    age=row['Age'],
                    color=row['Primary Fur Color'],
                    loc=row['Location'],
                    specific_loc=row['Specific Location'],
                    running=row['Running'],
                    chasing=row['Chasing'],
                    climbing=row['Climbing'],
                    eating=row['Eating'],
                    oraging=row['Foraging'],
                    other_act=row['Other Activities'],
                    kuks=row['Kuks'],
                    quaas=row['Quaas'],
                    moans=row['Moans'],
                    tail_flags=row['Tail flags'],
                    tail_twitches=row['Tail twitches'],
                    approaches=row['Approaches'],
                    indifferent=row['Indifferent'],
                    runs_from=row['Runs from']
                    )
            c=c+1
        self.stdout.write("File path: %s" % path)
        self.stdout.write("rows inserted: %s " % c)
