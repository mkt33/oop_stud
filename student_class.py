class Student:
	num_of_studs=0
	def __init__(self,name,course):
		self.name = name
		self.course = course
		Student.num_of_studs += 1
	def __del__(self):
		print("object <",self.name,"> deleted")
		Student.num_of_studs -= 1

st1 = Student('Anmol','Python')
st2 = Student('Bhuvan','C&C++')
print(st1.name,st2.name)
print(Student.num_of_studs)
del st1
print(st2.name)
print(Student.num_of_studs)
