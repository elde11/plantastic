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
class NameDescriptionMixin(models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )
    
    description = models.CharField(
        max_length=150,
        null=False, blank=True, default="",
        verbose_name="Description",
        help_text="",
    )
    class Meta:
        abstract = True
class ImageMixin(models.Model):
    image_url = models.URLField(
        verbose_name="Image URL",
        help_text="",

    )
    class Meta:
        abstract = True


class Category(NameDescriptionMixin, UserMixin, ImageMixin, models.Model):
    slug = models.SlugField(unique=True)
   
    
class Plant(NameDescriptionMixin, UserMixin, models.Model):
  
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
  
class Room(NameDescriptionMixin, UserMixin, models.Model):
   
    ROOMEXPOSURE_CHOICES = Plant.EXPOSURE_CHOICES
    room_exposure = models.CharField(
        max_length=10, choices=ROOMEXPOSURE_CHOICES,
        null=False, blank=False,
        verbose_name="Amount of sun",
        help_text="",
    )
    
    HUMIDITY_CHOICES = Plant.HUMIDITY_CHOICES 
    humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        null=False, blank=True,
        verbose_name="Humidity",
        help_text="",
    )
    
    TEMPERATURE_CHOICES = Plant.TEMPERATURE_CHOICES
    temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        null=False, blank=True,
        verbose_name="Room's Temperature",
        help_text="",
    )
    drafty = models.BooleanField(
        default=False,
        null=False, blank=True,
        verbose_name="Drafty?",
        help_text="",
    )
    
class UserPlant(NameDescriptionMixin, ImageMixin, UserMixin, models.Model): 
    plant = models.ForeignKey(
        Plant,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Type of Plant",
        help_text="",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Room",
        help_text="",
    )
    last_watered= models.DateTimeField(
        null=True,blank=True,
        verbose_name="Timestamp of last watering",
        help_text="",
    )
    last_fertilized = models.DateTimeField(
        null=True,blank=True,
        verbose_name="Timestamp of last fertilizing",
        help_text="",
    )
  