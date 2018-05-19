# dir(object name) lists the methods and fields of an object
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def print(self):
		print(self.arg)

#___________________________________________
#this class inherit from the previous class 
class  NewClass(ClassName):
	#to make it private write _ before it
	newclasses = 0

	def __init__(self, arg, typ):
		ClassName.__init__(self,arg)
		self.classtype = typ         #classtye is private type                    
		type(self).newclasses = type(self).newclasses + 1

	def setclassType(self, val):
		if(val == "none"):
			print("can't set by none value")
			return

		self._classtype = val

	def getClassType(self):
		return self._classtype

	classtype = property(getClassType, setclassType)

##############3
obj = NewClass(20, "ahmed")
print(obj.classtype)