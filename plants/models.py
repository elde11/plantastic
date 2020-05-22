from django.conf import settings
from django.db import models


class UserMixin(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="User",
        help_text="",
    )
    class Meta:
        abstract = True


class Category(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )
    slug = models.SlugField()
    description = models.CharField(
        max_lenght=150,
        null=False, blank=True, default="",
        verbose_name="Description",
        help_text="",
    )
    image_url = models.URLField(
        verbose_name="Image URL",
        help_text="",
    )
    
class Plant(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Category",
        help_text="",
    )
    watering_interval = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Watering interval",
        help_text="In seconds",
    )
    fertilizing_interval = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Fertilizing interval",
        help_text="In seconds",
    )
    EXPOSURE_CHOICES = [
        ("dark", "Dark"),
        ("shade", "Shade"),
        ("partsun", "Part sun"),
        ("fullsun", "Full sun"),
    ]
    required_exposure = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICES,
        null=False, blank=False,
        verbose_name="Amount of sun",
        help_text="",
    )
    HUMIDITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    required_humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        null=False, blank=False,
        verbose_name="Humidity",
        help_text="",
    )
    TEMPERATURE_CHOICES = [
        ("cold", "Cold"),
        ("medium", "Medium"),
        ("warm", "Warm"),
    ]
    required_temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        null=False, blank=False,
        verbose_name="Temperature",
        help_text="",
    )
    blooming = models.BooleanField(
        default=False,
        null=False, blank=True,
        verbose_name="Blooming?",
    )
    DIFFICULTY_CHOICES = [
        (1, "Low"),
        (2, "Medium-low"),
        (3, "Medium"),
        (4, "Medium-high"),
        (5, "high"),
    ]
    difficulty = models.PositiveIntegerField(
        choices=DIFFICULTY_CHOICES,
        null=False, blank=False, default=1,
        verbose_name="Cultivation difficulty level",
        help_text="",
    )
  
class Room(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,choices=EXPOSURE_CHOICES,
        null=False, blank=False,
    )
    HUMIDITY_CHOICES = [
		('low', 'Low'),
		('medium', 'Medium'),
		('high', 'High'),
	]
	humidity = models.CharField(
		max_length=10,
		choices=None,
		help_text="Optimal humidity"
	)

	TEMPERATURES_CHOICES = [
		('cold', 'Cold'),
		('medium', 'Medium'),
		('warm', 'Warm'),
	]
    required_temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        null=False, blank=False,
        verbose_name="Temperature",
        help_text="",
    )
    EXPOSURE_CHOICES = [
        ('dark', 'Dark'),
        ('shade', 'Shade'),
        ('partsun', 'Part Sun'),
        ('fullsun', 'Full Sun'),
    ]
    required_exposure = models.CharField(
        max_length=20, choices=EXPOSURE_CHOICES,
        null=False, blank=False,
        verbose_name="Amount of sun",
        help_text="",
     )
    watering_interval = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Watering interval",
        help_text="In seconds",
    )
    drafty = models.BooleanField(
        default=False,
        null=False, blank=True,
        verbose_name="Drafty?",
    )
    
class UserPlant(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )
    description = models.CharField(
        max_lenght=155,
        null=False, blank=True, default="",
        verbose_name="Description",
        help_text="",
    )
    required_humidity = models.CharField(
        max_length=20, choices=HUMIDITY_CHOICES,
        null=False, blank=False,
        verbose_name="Humidity",
        help_text="",
    )
    plant = models.ForeignKey(
        Plant,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Plant",
        help_text="",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
    )
    last_watering = models.DateTimeField()

    last_fertilizing = models.DateTimeField()