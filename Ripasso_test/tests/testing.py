import unittest
from Ripasso.ripasso import Calc

class TestCalculations(unittest.TestCase):

    def setUp(self) -> None:
        self.calcolo=Calc(4,4)
    
    def test_get_sum(self):
        self.assertEqual(self.calcolo.get_sum(), 8 , "Il calcolo e sbagliato")

if __name__ == "__main__":
    unittest.main()