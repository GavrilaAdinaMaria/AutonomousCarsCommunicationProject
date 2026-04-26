import unittest
from AutonomousCarsCommunication.AutonomousCarsCommunication import AutonomousCarsCommunication

class TestAutonomousCars(unittest.TestCase):

    def setUp(self):
        # Reset the class variable before each test to ensure a clean slate
        AutonomousCarsCommunication.cars_list = []
        self.car1 = AutonomousCarsCommunication("Audi", "Q5", 100)

    # --- Validation Tests ---
    def test_invalid_manufacturer(self):
        with self.assertRaises(ValueError):
            AutonomousCarsCommunication(12345, "Model S", 200)

    def test_negative_id(self):
        with self.assertRaises(ValueError):
            AutonomousCarsCommunication("Tesla", "Model 3", -1)

    # --- Speed Logic Tests ---
    def test_speed_limit_high(self):
        self.car1.set_car_speed(350) # Invalid
        self.assertEqual(self.car1.speed, 0) # Should remain 0

    def test_speed_limit_low(self):
        self.car1.set_car_speed(-10) # Invalid
        self.assertEqual(self.car1.speed, 0)

    # --- Communication & Math Tests ---
    def test_distance_calculation(self):
        car2 = AutonomousCarsCommunication("Tesla", "Model 3", 200)
        self.car1.set_car_location(0, 0)
        car2.set_car_location(3, 4)
        # 3-4-5 Triangle: sqrt(3^2 + 4^2) = 5
        self.assertEqual(self.car1.calculate_distance(car2), 5.0)

    def test_closest_car(self):
        self.car1.set_car_location(0, 0)
        self.car1.add_car()
        
        car_near = AutonomousCarsCommunication("Near", "Car", 2)
        car_near.set_car_location(1, 1)
        car_near.add_car()
        
        car_far = AutonomousCarsCommunication("Far", "Car", 3)
        car_far.set_car_location(100, 100)
        car_far.add_car()
        
        closest = self.car1.pick_closest_car()
        self.assertEqual(closest.carID, 2)

if __name__ == '__main__':
    unittest.main()