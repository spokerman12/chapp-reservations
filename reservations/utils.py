from .validators import (
    validate_check_in,
    validate_check_in_out,
    validate_check_out,
)
from .models import RoomType, Room, Reservation

from datetime import datetime


ROOM_TYPES = list(obj["name"] for obj in RoomType.objects.values("name"))


def get_occupied_rooms(check_in: str, check_out: str, num_guests: int) -> list:
    check_in_dt = datetime.date(datetime.strptime(check_in, "%Y-%m-%d"))
    check_out_dt = datetime.date(datetime.strptime(check_out, "%Y-%m-%d"))
    return [
        reservation.room
        for reservation in Reservation.objects.filter(
            check_in__gte=check_in_dt,
            check_in__lte=check_out_dt,
            check_out__gte=check_in_dt,
            check_out__lte=check_out_dt,
            room__room_type__max_capacity__gte=num_guests,
        )
    ]


def overlapping_reservations(room_id, check_in, check_out):
    return Reservation.objects.filter(
        room_id=room_id,
        check_in__gte=check_in,
        check_in__lte=check_out,
    ) | Reservation.objects.filter(
        room_id=room_id, check_out__gte=check_in, check_out__lte=check_out
    )


def get_price(check_in: str, check_out: str, room_type: str):

    try:
        per_night = str(RoomType.objects.get(name=room_type).price_per_night)
    except RoomType.DoesNotExist:
        per_night = "€0.00"

    check_in_dt = datetime.date(datetime.strptime(check_in, "%Y-%m-%d"))
    check_out_dt = datetime.date(datetime.strptime(check_out, "%Y-%m-%d"))
    days = (check_out_dt - check_in_dt).days
    full_price = int(days) * float(per_night[1:])

    return {"per_night": per_night, "full_price": full_price}


def get_offers(
    check_in: str, check_out: str, num_guests: int, show_one_of: bool = False
) -> list:

    validate_check_in(check_in)
    validate_check_out(check_out)
    validate_check_in_out(check_in, check_out)

    occupied_room_numbers = [
        room.number for room in get_occupied_rooms(check_in, check_out, num_guests)
    ]

    vacancies_in_date_range = Room.objects.filter(
        room_type__max_capacity__gte=num_guests
    ).exclude(number__in=occupied_room_numbers)

    for vacancy in vacancies_in_date_range:
        price = get_price(check_in, check_out, vacancy.room_type.name)
        vacancy.per_night = price["per_night"]
        vacancy.full_price = "%.2f" % price["full_price"]

    offers = list(vacancies_in_date_range)

    if show_one_of:
        offers = []
        for room_type in ROOM_TYPES:
            offer = next(
                (
                    room
                    for room in vacancies_in_date_range
                    if room.room_type.name == room_type
                ),
                None,
            )
            offers.append(offer)

    return offers
