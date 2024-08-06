import sys
import unittest
import os
from model_v2 import train_svm
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestModel(unittest.TestCase):

    def test_model_training(self):
        print("Running test_model_training")
        model = train_svm()
        self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()
