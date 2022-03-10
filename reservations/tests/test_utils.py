from django.test import TestCase

from reservations.models import Reservation, Room, RoomType
from reservations.utils import get_occupied_rooms, get_price, overlapping_reservations


class TestUtils(TestCase):
    def setUp(self):
        self.type_a = RoomType.objects.create(
            name="A", max_capacity=1, price_per_night=20
        )
        self.type_b = RoomType.objects.create(
            name="B", max_capacity=2, price_per_night=30
        )
        self.type_c = RoomType.objects.create(
            name="C", max_capacity=3, price_per_night=40
        )
        self.room_1 = Room.objects.create(room_type_id=self.type_a.id)
        self.room_2 = Room.objects.create(room_type_id=self.type_b.id)
        self.room_3 = Room.objects.create(room_type_id=self.type_c.id)
        self.res_1 = Reservation.objects.create(
            contact_name="John",
            email="john@son.com",
            phone_number=123123,
            check_in="2022-04-04",
            check_out="2022-04-05",
            cost=20,
            room=self.room_1,
            valid=True,
            num_guests=1,
        )
        self.res_2 = Reservation.objects.create(
            contact_name="Gun",
            email="gun@ner.com",
            phone_number=123123,
            check_in="2022-04-05",
            check_out="2022-04-06",
            cost=20,
            room=self.room_2,
            valid=True,
            num_guests=2,
        )
        self.res_3 = Reservation.objects.create(
            contact_name="Bub",
            email="bub@ba.com",
            phone_number=123123,
            check_in="2022-04-06",
            check_out="2022-04-07",
            cost=20,
            room=self.room_3,
            valid=True,
            num_guests=3,
        )

    def test_get_occupied_rooms(self):
        self.assertTrue(
            self.room_1 in get_occupied_rooms("2022-04-04", "2022-04-05", 1)
        )
        self.assertTrue(
            self.room_2 not in get_occupied_rooms("2022-04-04", "2022-04-05", 1)
        )
        self.assertTrue(
            self.room_3 not in get_occupied_rooms("2022-04-04", "2022-04-05", 1)
        )

    def test_overlapping_reservations(self):
        self.assertFalse(
            overlapping_reservations(self.room_1.number, "2022-04-02", "2022-04-03")
        )
        self.assertTrue(
            any(
                overlapping_reservations(self.room_1.number, "2022-04-03", "2022-04-04")
            )
        )
        self.assertTrue(
            any(
                overlapping_reservations(self.room_1.number, "2022-04-04", "2022-04-05")
            )
        )
        self.assertTrue(
            overlapping_reservations(self.room_1.number, "2022-04-05", "2022-04-06")
        )
        self.assertFalse(
            overlapping_reservations(self.room_1.number, "2022-04-06", "2022-04-07")
        )

    def test_get_price(self):
        self.assertEqual(
            get_price("2022-04-02", "2022-04-03", "A"),
            {"per_night": "€20.00", "full_price": 20.0},
        )
        self.assertEqual(
            get_price("2022-04-02", "2022-04-04", "A"),
            {"per_night": "€20.00", "full_price": 40.0},
        )

    # def test_get_offers(self):
    #     self.assertTrue(
    #         room_1get_offers("2022-04-04","2022-04-05", 1, False)
    #     )
