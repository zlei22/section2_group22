from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):

    # Latitude
    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=19,
        decimal_places=15,
        )
    
    # Longitude
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
    
    # Shift
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        help_text=_('Shift'),
        max_length=16,
        choices=SHIFT_CHOICES,
    )

    # Date
    date = models.DateField(
        help_text=_('Date'),
    )
    
    # Age
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
        help_text=_('Age'),
        max_length=16,
        choices=AGE_CHOICES,
        blank=True,
    )
