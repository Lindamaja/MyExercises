class Parent(object):

	def override(self):
		pass
		
class Child(Parent):

	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()