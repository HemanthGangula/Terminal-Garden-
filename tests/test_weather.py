import unittest
from terminal_garden.weather import Weather

class TestWeather(unittest.TestCase):
    def setUp(self):
        self.weather = Weather()

    def test_initial_weather(self):
        self.assertIsNone(self.weather.current_weather)

    def test_generate_weather(self):
        generated_weather = self.weather.generate_weather()
        self.assertIn(generated_weather, ['Sunny', 'Rainy', 'Drought', 'Storm'])
        self.assertEqual(self.weather.current_weather, generated_weather)

    def test_get_current_weather(self):
        self.weather.generate_weather()
        self.assertEqual(self.weather.get_current_weather(), self.weather.current_weather)

if __name__ == '__main__':
    unittest.main()