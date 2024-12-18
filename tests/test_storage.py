import unittest
from terminal_garden.storage import Storage
from terminal_garden.plant import Plant
import os

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage('test_garden_state.json')
        self.plant = Plant()

    def tearDown(self):
        if os.path.exists(self.storage.filepath):
            os.remove(self.storage.filepath)

    def test_save(self):
        self.plant.stage = 3
        self.plant.health = 90
        self.storage.save(self.plant)
        self.assertTrue(os.path.exists(self.storage.filepath))

    def test_load_existing_file(self):
        # Save a state first
        self.plant.stage = 2
        self.plant.health = 85
        self.storage.save(self.plant)
        loaded_state = self.storage.load()
        self.assertIsNotNone(loaded_state)
        self.assertEqual(loaded_state['stage'], 2)
        self.assertEqual(loaded_state['health'], 85)

    def test_load_no_file(self):
        if os.path.exists(self.storage.filepath):
            os.remove(self.storage.filepath)
        loaded_state = self.storage.load()
        self.assertIsNone(loaded_state)

if __name__ == '__main__':
    unittest.main()