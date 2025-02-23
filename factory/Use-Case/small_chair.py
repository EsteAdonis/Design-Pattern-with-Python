# pylint: disable=too-few-public-methods
"A Class of Chair"
from interface_chair import IChair

class SmallChair(IChair):
  "The Small Chair Concrete Class implements the IChair interface"
  def __init__(self):
      self._height = 40
      self._width = 40
      self._depth = 40

  def get_dimensions(self) -> str:
    return {
       "width": self._width,
       "depth": self._depth,  
       "height": self._height
    }
