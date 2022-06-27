from django.contrib import admin
from . import models


@admin.register(models.Amenity, models.RoomRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definiton"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definiton"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definiton"""

    list_display = (
        "name",
        "max_guests",
        "beds",
        "bedrooms",
        "bathrooms",
    )

    search_fields = ("name",)
