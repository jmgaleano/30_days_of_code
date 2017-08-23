#Class Vs. Instance
#class Person:
#	def __init__(self,initialAge):
#		# Add some more code to run some checks on initialAge
#	def amIOld(self):
#		# Do some computations in here and print out the correct statement to the console
#	def yearPasses(self):
#		# Increment the age of the person in here      

#class Person:
#	def __init__(self,initialAge):
initialAge = (int(input()))
if initialAge < 0:
	initialAge = 0
	print("Age is not valid, setting age to 0...")
else:
	age = initialAge
print (age)
