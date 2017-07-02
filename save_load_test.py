import unittest
from save_load import File


class TestSaveLoad(unittest.TestCase):
    def test_init(self):
        file = File()

    def test_load(self):
        file = File("C:/Users/Megg/Programs/Python/Once a Day Daily Habit Tracker Planner/saves/test.csv")
        file.load()


if __name__ == '__main__':
    unittest.main()
