class DateTime(object):

	def __init__(self, day=10, month=10, year=2000):
		self.day = day
		self.month = month
		self.year = year

	@classmethod
	def from_string(cls, string_date):
		day, month, year = map(int, string_date.split('-'))
		myDate = cls(day, month, year)
		return myDate
dateObj = DateTime.from_string('20-05-1994')
print(dateObj.day)
print(dateObj.month)
print(dateObj.year)