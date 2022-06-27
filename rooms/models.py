from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):

    """Amenity Types"""

    class Meta:
        verbose_name_plural = "Amenities"


class RoomRule(AbstractItem):

    """Room Rules"""

    class Meta:
        verbose_name = "Room Rule"


class Photo(AbstractItem):

    """Photo Object Definition"""

    photo = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        def __str__(self):
            return self.name


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140, null=True)
    description = models.TextField(null=True)
    max_guests = models.IntegerField(default=2)
    beds = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    livingrooms = models.IntegerField(default=0)
    size = models.IntegerField(null=True)
    bathrooms = models.IntegerField(default=1)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    room_rules = models.ManyToManyField("RoomRule", blank=True)

    def __str__(self):
        return self.name
