# inheritance : 

class Robot:
    def action(self):
        print('Robot action')
        self.name='A13'
class RobotR:
	def action(self):
		print("RobotR action")
class HelloRobot(Robot):
    def action(self):
        print('Hello world')
class DummyRobot(Robot, RobotR):
    def start(self):
        print('Started.')
    def action(self):
    	print("hello from dummy robot")
    	
r = HelloRobot()
d = DummyRobot()
print('-------------')
r.action()
print('-------------')
d.action()
# print(d.name)