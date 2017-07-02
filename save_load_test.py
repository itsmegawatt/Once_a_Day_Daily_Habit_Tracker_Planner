import unittest
from save_load import File


class TestSaveLoad(unittest.TestCase):
    def test_init(self):
        file = File()

    def test_load(self):
        self.file.load("C:/Users/Megg/Programs/Python/Once a Day Daily Habit Tracker Planner/saves/test.csv")


if __name__ == '__main__':
    unittest.main()
