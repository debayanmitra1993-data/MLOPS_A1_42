import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from model_v2 import train_decision_tree

class TestModel(unittest.TestCase):

    def test_model_training(self):
        print("Running test_model_training")
        model = train_decision_tree()
        self.assertIsNotNone(model)

if __name__ == "__main__":
    unittest.main()