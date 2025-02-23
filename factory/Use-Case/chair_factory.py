from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory: # pylint: disable=too-few-public-methods
  "The Factory Class"

  @staticmethod
  def get_chair(chair_type: str):
    "A static method to get a chair"
    try:
        if chair_type == "SmallChair":
            return SmallChair()
        if chair_type == "MediumChair":
            return MediumChair()
        if chair_type == "BigChair":
            return BigChair()
        raise AssertionError("Chair Not Found")
    except AssertionError as _e:
        print(_e)
        return None