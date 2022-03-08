from .models import Reservation, RoomType, Room, Client
from django.contrib import admin

admin.site.register(Reservation)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Client)
