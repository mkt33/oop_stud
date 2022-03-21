# derived/child class:
# inheritance: 

class Robot:
   def __init__(self):
      self.name = "Rbt-B Alpha" # robot base alpha
      self._created_on = "2020/11/25" # protected attribute
      self.__version = 1.0	# encapsulation with __varible -> private attribute
   def ability(self):
      print(" is able to communicate with human.")

class RobotBeta(Robot):
   name = "Rbt-D Beta"
   def ability(self):
     print("can help human")

r = Robot()
r.ability()
rb = RobotBeta()
rb.ability()
