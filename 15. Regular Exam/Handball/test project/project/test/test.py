from unittest import TestCase
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip1 = Trip(1000, 5, True)

    def test_initialisation(self):
        self.assertEqual(1000, self.trip1.budget)
        self.assertEqual(5, self.trip1.travelers)
        self.assertEqual(True, self.trip1.is_family)

    def test_travelers_less_than_1_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.trip1.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_is_family_raises(self):
        self.trip1.travelers = 2
        self.trip1.is_family = False
        self.assertEqual(False, self.trip1.is_family)






