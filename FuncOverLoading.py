# Method overloading is just make some arguments optional thats it.

class OverLoading():
    def __init__(self):
        self.value="this is overloading example"     
    def ovrld(self,val1=None,val2=None):
        self.first=val1
        self.second=val2
        if val2 is None:
            return self.first
        elif val1 is None:
            return self.second
        elif val1 is None and val2 is None:
            return None
        else:
            return self.first,self.second
    # def ovrld(self,val1,val2):
    #     self.val1=val1
    #     self.val2=val2
    #     return self.val1,self.val2

obj=OverLoading()
print(obj.ovrld(10)) # integer argument
print(obj.ovrld("this is my first call of the funtion")) # one string argument
print(obj.ovrld("this is my second call of the first value","this is mysecond call of second val")) # two string argument
