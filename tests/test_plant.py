import unittest
from terminal_garden.plant import Plant
from io import StringIO
import sys

class TestPlant(unittest.TestCase):
    def setUp(self):
        self.plant = Plant()

    def test_initial_state(self):
        self.assertEqual(self.plant.stage, 0)
        self.assertEqual(self.plant.health, 100)

    def test_grow(self):
        self.plant.grow()
        self.assertEqual(self.plant.stage, 1)

    def test_water(self):
        self.plant.water()
        self.assertEqual(self.plant.health, 110)

    def test_status_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.plant.status()
        sys.stdout = sys.__stdout__
        self.assertIn("Stage: 0, Health: 100", captured_output.getvalue())

    def test_apply_weather_sunny(self):
        self.plant.apply_weather_effect('Sunny')
        self.assertEqual(self.plant.health, 105)

    def test_apply_weather_rainy(self):
        self.plant.apply_weather_effect('Rainy')
        self.assertEqual(self.plant.health, 110)

    def test_apply_weather_drought(self):
        self.plant.apply_weather_effect('Drought')
        self.assertEqual(self.plant.health, 85)

    def test_apply_weather_storm(self):
        self.plant.apply_weather_effect('Storm')
        self.assertEqual(self.plant.health, 80)

if __name__ == '__main__':
    unittest.main()