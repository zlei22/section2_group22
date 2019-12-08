# This is an export command.

from django.core.management.base import BaseCommand
from sightings.models import Sighting
import csv
import sys

class Command(BaseCommand):
    help = 'export data'

    def add_arguments(self,parser):
        parser.add_argument('csv_file')

    def handle(self,*args,**options):

        with open(options['csv_file'], 'w', newline='')as fp:
            export_data = csv.writer(fp, delimiter='\t')
            fields = [f.name for f in Sighting._meta.fields]
            export_data.writerow(fields)
            for line in Sighting.objects.all():
                export_data.writerow([getattr(line,i) for i in fields])

