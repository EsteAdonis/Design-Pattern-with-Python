# The Abstract Factory Pattern adds an abstraction layer over multiple other creational pattern 
# implementations.
# https://sbcode.net/python/abstract_factory/


# pylint: disable=too-few-public-methods
"Abstract Factory Concept Sample Code"
from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB

class IAbstractFactory(metaclass=ABCMeta):
  "Abstract Factory Interface"
  
  @staticmethod
  @abstractmethod
  def create_object(factory) -> str:
    "The static Abstract factory interface method"


class AbstractFactory(IAbstractFactory):
  "The Abstract Factory Concrete Class"

  @staticmethod
  def create_object(factory) -> str:
    "Static get_factory method"
    try:
      if factory in ['aa', 'ab', 'ac']:
        return FactoryA().create_object(factory[1])
      if factory in ['ba', 'bb', 'bc']:
        return FactoryB().create_object(factory[1])
      raise AssertionError("No Factory Found")
    except AssertionError as _e:
      print(_e)
      return None
    
# The Client
Product = AbstractFactory.create_object("bc")
print(f"{Product.__class__})")

Product = AbstractFactory.create_object("aa")
print(f"{Product.__class__})")