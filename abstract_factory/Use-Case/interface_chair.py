# pylint: disable=too-few-public-methods
"Abstract Chair Factory"

from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
  "Abstract Chair Interface"
  
  @staticmethod
  @abstractmethod
  def get_dimensions(chair) -> str:
    "The static Abstract Chair interface method"