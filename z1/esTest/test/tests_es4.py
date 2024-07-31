import unittest
from esercizi.es1 import Cane ,Gatto

class testAnimali(unittest.TestCase):
    def setUp(self):
        self.cane= Cane("pluto" , "cane" , 12 , "bau")
        self.gatto= Gatto("silvestro" , "gatto " ,7 ,"miao")

    def test_verso(self):
        
    
        self.assertEqual(self.cane.fai_suono() , "bau" , "il verso del cane e sbagliato")
        self.assertEqual(self.gatto.fai_suono() , "miao", "il verso del gatto e sbagliato")

if __name__ == "__main__":
    unittest.main()