"The Chair Factory Class"
from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:
  "The Chair Factory Concrete Class"

  @staticmethod
  def get_chair(chair) -> str:
    "Static get_factory method"
    try:
      if chair == 'SmallChair':
        return SmallChair()
      if chair == 'MediumChair':
        return MediumChair()
      if chair == 'BigChair':
        return BigChair()
      raise AssertionError("No Chair Factory Found")
    except AssertionError as _e:
      print(_e)
      return None