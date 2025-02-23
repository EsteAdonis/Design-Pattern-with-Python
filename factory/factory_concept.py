# The Factory pattern is really about adding that extra abstraction 
# between the object creation and where it is used. 
# This gives you extra options that you can more easily extend in the future.

# pyline: disable=too-few-public-methods
# pylint: disable=argument-differ
"The factory Conecpt"
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
  "A Hypothetical Class Interface (Product)"
  
  @staticmethod
  @abstractmethod
  def create_object(self) -> str:
      "An abstract interface method"

class ConcreteProductA(IProduct):
  "A Concrete Class that implements the IProduct interface"
  def __init__(self):
      self.name = "ConcreteProductA"

  def create_object(self) -> str:
      return self
  
class ConcreteProductB(IProduct):
  "A Concrete Class that implements the IProduct interface"
  def __init__(self):
      self.name = "ConcreteProductB"

  def create_object(self) -> str:
      return self

class ConcreteProductC(IProduct):
  "A Concrete Class that implements the IProduct interface"
  def __init__(self):
      self.name = "ConcreteProductC"

  def create_object(self) -> str:
      return self

class Creator:
  "The Factory Class"
  
  @staticmethod
  def create_object(some_property: str) -> IProduct:
      "A static method to get a concrete product"
      if some_property == "a":
          return ConcreteProductA()
      if some_property == "b":
          return ConcreteProductB()
      if some_property == "c":
          return ConcreteProductC()
      return None

# The Client
Product = Creator.create_object("b")
print(Product.name)
Product = Creator.create_object("c")
print(Product.name)