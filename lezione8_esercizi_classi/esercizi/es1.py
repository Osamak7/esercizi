"""
Exercise 1: Creating an Abstract Class with Abstract Methods
Create an abstract class Shape with an abstract method area and
 another abstract method perimeter. Then, create two subclasses
   Circle and Rectangle that implement the area and perimeter methods."""

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass
    @abstractmethod
    def perimeter(self) -> float :
        pass

class Circle(Shape):
    
    def __init__(self, raggio:float) -> None:
        self.raggio=raggio
    
    def area(self) : 
        area :float = math.pi *(self.raggio **2 )
        return area
    
    def perimeter(self):
        perimetro = (2 * math.pi)* self.raggio
        return perimetro
    
class Rectangle(Shape):

    def __init__(self, base:int , altezza: int) -> None:
        self.base=base
        self.altezza=altezza

    def area(self ):
        area : int = self.base * self.altezza
        return area
    
    def perimeter(self):
        perimetro : int= (2 * self.base) + (2 * self.altezza)
        return perimetro