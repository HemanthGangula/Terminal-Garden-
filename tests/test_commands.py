import unittest
from terminal_garden.commands import CommandHandler
from terminal_garden.plant import Plant
from terminal_garden.weather import Weather
from terminal_garden.storage import Storage
from io import StringIO
import sys
import os

class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.plant = Plant()
        self.weather = Weather()
        self.storage = Storage('test_garden_state.json')
        self.command_handler = CommandHandler(self.plant, self.weather, self.storage)

    def tearDown(self):
        if os.path.exists(self.storage.filepath):
            os.remove(self.storage.filepath)

    def test_handle_plant_seed(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.command_handler.handle('plant seed')
        sys.stdout = sys.__stdout__
        # Assuming 'plant seed' initializes or reinitializes Plant
        self.assertEqual(self.plant.stage, 0)  # initial stage
        self.assertIn("A new seed has been planted.", captured_output.getvalue())
        self.assertTrue(os.path.exists(self.storage.filepath))

    def test_handle_water(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.command_handler.handle('plant seed')
        self.command_handler.handle('water')
        sys.stdout = sys.__stdout__
        self.assertEqual(self.command_handler.plant.health, 110)
        self.assertIn("Plant has been watered.", captured_output.getvalue())

    def test_handle_status(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.command_handler.handle('status')
        sys.stdout = sys.__stdout__
        self.assertIn("Stage: 0, Health: 100", captured_output.getvalue())

    def test_handle_weather(self):
        self.command_handler.handle('weather')
        # Since generate_weather is random, just ensure current_weather is set
        self.assertIsNotNone(self.weather.current_weather)

    def test_handle_save_load(self):
        # Modify plant state
        self.command_handler.plant.stage = 3
        self.command_handler.plant.health = 80
        # Handle save command
        self.command_handler.handle('save')
        # Load state and verify
        saved_state = self.storage.load()
        loaded_plant = Plant(stage=saved_state.get('stage', 0), health=saved_state.get('health', 100))
        self.assertEqual(loaded_plant.stage, 3)
        self.assertEqual(loaded_plant.health, 80)

    def test_handle_reset_yes(self):
        # Modify plant state
        self.plant.stage = 5
        self.plant.health = 90
        # Simulate user input 'yes'
        captured_output = StringIO()
        sys.stdout = captured_output
        sys.stdin = StringIO('yes\n')
        self.command_handler.handle('reset')
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertEqual(self.plant.stage, 0)
        self.assertEqual(self.plant.health, 100)
        self.assertIn("Garden has been reset.", captured_output.getvalue())

    def test_handle_reset_no(self):
        # Modify plant state
        self.plant.stage = 5
        self.plant.health = 90
        # Simulate user input 'no'
        captured_output = StringIO()
        sys.stdout = captured_output
        sys.stdin = StringIO('no\n')
        self.command_handler.handle('reset')
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertEqual(self.plant.stage, 5)
        self.plant.health  # Ensure no changes
        self.assertEqual(self.plant.health, 90)
        self.assertIn("Reset canceled.", captured_output.getvalue())

    def test_handle_help(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.command_handler.handle('help')
        sys.stdout = sys.__stdout__
        self.assertIn("Available Commands:", captured_output.getvalue())
        self.assertIn("plant seed", captured_output.getvalue())
        self.assertIn("water", captured_output.getvalue())
        self.assertIn("status", captured_output.getvalue())
        self.assertIn("weather", captured_output.getvalue())
        self.assertIn("save", captured_output.getvalue())
        self.assertIn("load", captured_output.getvalue())
        self.assertIn("reset", captured_output.getvalue())
        self.assertIn("help", captured_output.getvalue())
        self.assertIn("exit", captured_output.getvalue())

    def test_handle_exit(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        # Simulate exit by raising SystemExit
        with self.assertRaises(SystemExit):
            self.command_handler.handle('exit')
        sys.stdout = sys.__stdout__
        self.assertIn("Exiting Terminal Garden. Goodbye!", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()