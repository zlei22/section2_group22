from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Sighting(models.Model):

    # Latitude
    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=19,
        decimal_places=15,
        )
    
    # Longtitude
    longtitude = models.DecimalField(
        help_text=_('Longtitude'),
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

    # Primary Fur Color
    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMON = 'Cinnamon'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (BLACK, 'Black'),
        (CINNAMON, 'Cinnamon'),
    )

    color = models.CharField(
        help_text=_('Primary Fur Color'),
        max_length=16,
        choices=COLOR_CHOICES,
        blank=True,
    )

    # Location
    ABOVE = 'Above Ground'
    PLANE = 'Ground Plane'

    LOC_CHOICES = (
        (ABOVE, 'Above Ground'),
        (PLANE, 'Ground Plane'),
    )

    loc = models.CharField(
        help_text=_('Location'),
        max_length=20,
        choices=LOC_CHOICES,
        blank=True,
    )
    
    # Specific Location
    specific_loc = models.CharField(
        help_text=_('Specific Location'),
        max_length=255,
        blank=True,
    )

    # Running
    running = models.BooleanField(
        help_text=_('Running'),
        default=False,
    )

    # Chasing
    chasing = models.BooleanField(
        help_text=_('Chasing'),
        default=False,
    )

    # Climbing
    climbing = models.BooleanField(
        help_text=_('Climbing'),
        default=False,
    )

    # Eating
    eating = models.BooleanField(
        help_text=_('Eating'),
        default=False,
    )

    # Foraging
    foraging = models.BooleanField(
        help_text=_('Foraging'),
        default=False,
    )

    # Other Activities
    other_act = models.CharField(
        help_text=_('Other Activities'),
        max_length=255,
        blank=True,
    )

    # Kuks
    kuks = models.BooleanField(
        help_text=_(‘Kuks’),
        default=False,
    )
    
    # Quaas
    quaas = models.BooleanField(
        help_text=_('Quaas'),
        default=False,
    )

    # Moans
    moans = models.BooleanField(
        help_text=_('Moans'),
        default=False,
    )
    
    # Tail Flags
    tail_flags = models.BooleanField(
        help_text=_('Tail flags'),
        default=False,
    )
    
    # Tail Twitches
    tail_twitches = models.BooleanField(
        help_text=_('Tail twitches'),
        default=False,
    )
    
    # Approaches
    approaches = models.BooleanField(
        help_text=_('Approaches'),
        default=False,
    )
    
    # Indifferent
    indifferent = models.BooleanField(
        help_text=_('Indifferent'),
        default=False,
    )
    
    # Runs From
    runs_from = models.BooleanField(
        help_text=_('Runs from'),
        default=False,
    )

    def __str__(self):
        return self.uid

