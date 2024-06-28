import unittest 
import math
from esercizi.es1 import Circle,Rectangle
from esercizi.es2 import MathOperations

class Test_es1(unittest.TestCase):
    #Circle
    def test_area_circle(self):
        circle = Circle(5)
        #plages = 5 lo utilizzo perche coi numeri con la virgola lunghi confronto solo i primi 5
        self.assertAlmostEqual(circle.area(), math.pi *(5 **2 ) , places=5, msg="L'area del cerchio e sbagliata")

    def test_perimetro_circle(self):
        circle= Circle(5)
        self.assertAlmostEqual(circle.perimeter(), (2 * math.pi)* 5 , places=5 , msg="Il perimetro e sbagliato")
    #Rectangle
    def test_area_rectangle(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20 , "L'area del triangolo e sbagliata")

    def test_perimetro_rectangle(self):
        rectangle= Rectangle(4,5) # 4*2= 8 +  5*2=10 = 18 
        self.assertEqual(rectangle.perimeter() , 18 ,"Il calcolo del perimetro e sbagliato" )

class Test_es2(unittest.TestCase):
    def tests_add(self):
        somma= MathOperations()
        self.assertEqual(somma.add(a=5 ,b= 7) , 12 , "la somma non e corretta")

    def tests_multiply(self):
        moltiplicazione= MathOperations()
        self.assertEqual(moltiplicazione.multiply(a=7, b=3) , 21 , "la moltiplicazione non e corretta") 

if __name__ == "__main__":
    unittest.main()