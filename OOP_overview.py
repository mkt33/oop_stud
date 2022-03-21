"""
1. OOP overview
2. class and objects
	◦ Access Control (private , public and protected [on encapsulation ])
	◦ Data members, Member functions

3. Constructor, Destructor
4. Polymorphism
	◦ Overloading
		▪ Function Overloading
		▪ Operator Overloading
	◦ Overriding
		▪ Function Overriding -> with derived class
5. Inheritance
	◦ Base / Parent class
	◦ Derived / Child class
6. Encapsulation
7. Regular/instance method, Static method, Class method 
8. @property method
8. Setter and getter methods

"""


class display:
	def output(self):
		self.msg = "welcome to python class"
		print("hello world !")
	def output(self, msg=0)

disp = display() # creating an object of class display
disp.output() # calling method



