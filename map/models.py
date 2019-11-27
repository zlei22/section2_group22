from django.db import models
from django.utils.translation import gettext as _

class Squirrels(models.Model):

    # Latitude
    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=19,
        decimal_places=15,
        )
    
    # Longtitude
    longitude = models.DecimalField(
        help_text=_('Longitude'),
        max_digits=19,
        decimal_places=15,
    )

    # Unique Squirrel ID
    uid = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=255,
        primary_key=True,
    )  
