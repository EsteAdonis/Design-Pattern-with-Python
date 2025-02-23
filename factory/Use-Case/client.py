"Factory Use Case Example Code"

from chair_factory import ChairFactory

#The Client
Chair = ChairFactory.get_chair("SmallChair")
print(Chair.get_dimensions())