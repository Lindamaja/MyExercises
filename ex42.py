## Animal is-a object
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		##
		self.name = name

##cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		##
		self.name = name

##person is-a object
class Person(object):

	def __init__(self,name):
		##
		self.name = name
		
		## Person has-a pet of some 
		self.pet = None
		
##employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
	##
	super(employee, self).__init__(name)
	##employee has-a salary
	self.salary = salary
	
## fish is=a object
class Fish(object):
	pass
	
##salmon is-a fish
class Salmon(Fish):
	pass
	
##halibut is-a fish
class Halibut(Fish):
	pass

	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

##satan is marys pet
mary.pet = satan

##frank is-a employee, has-a salary of 120 000
frank = Employee("Frank",120000)

##frank has-a pet called rover
frank.pet = rover

##flipper is a fisch
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

##harry is a halibut
harry = Halibut()