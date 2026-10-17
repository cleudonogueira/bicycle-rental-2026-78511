import unittest
from bicycle import Bicycle

class TestBicycle(unittest.TestCase):

    def setUp(self):
        self.bike = Bicycle("T1", "Test Bike", 4.0)

    def test_create_bicycle(self):
        self.assertEqual(self.bike.item_id, "T1")
        self.assertEqual(self.bike.model, "Test Bike")
        self.assertFalse(self.bike.is_rented)

    def test_borrow_bicycle(self):
        self.assertTrue(self.bike.borrow_item())
        self.assertTrue(self.bike.is_rented)

    def test_borrow_already_rented(self):
        self.bike.borrow_item()
        self.assertFalse(self.bike.borrow_item())

    def test_return_bicycle(self):
        self.bike.borrow_item()
        self.assertTrue(self.bike.return_item())
        self.assertFalse(self.bike.is_rented)

    def test_calculate_cost(self):
        cost = self.bike.calculate_rental_cost(3)
        self.assertEqual(cost, 12.0)

    def test_invalid_rate_raises_error(self):
        with self.assertRaises(ValueError):
            Bicycle("T2", "Bad Bike", -5.0)

    def test_invalid_hours_raises_error(self):
        with self.assertRaises(ValueError):
            self.bike.calculate_rental_cost(0)

    def test_class_method(self):
        bike_str = Bicycle.from_string("T3, City Bike, 6.0")
        self.assertEqual(bike_str.item_id, "T3")
        self.assertEqual(bike_str.hourly_rate, 6.0)

if __name__ == "__main__":
    unittest.main()