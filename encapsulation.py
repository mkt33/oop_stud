# Access specifier: public, private, protected
# public access specifier:  var_pub = None -> No underscore or dunder -> access from anywhere.
# private access specifier: __var_pvt = None -> with dunder  -> access from only from the sameclass.
# protected access specifier: _var_ptt = None -> with under -> access from same class and derived class.

class RobotEx:
#class RobotEx(object):
   def __init__(self):
#      print(object)
      self.a = 123
      self._b = 123 # protected -> study on derived class
      self.__c = 123	# encapsulation with __varible
class Robot:
# class Robot(object):
   def __init__(self):
      self.__version = 22 # encapsuled with dunder variable

   def getVersion(self):	# getter interface
      print("version:",self.__version) 

   def setVersion(self, version):	# setter interface
      self.__version = version


obj1 = RobotEx()
print("a:",obj1.a)
print("b:",obj1._b)
# code below can not be executed because of encapsulation---requires interface 
# print(obj1.__c) 


obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
# code below can not be executed because of encapsulation---requires interface 
# print(obj.__version)