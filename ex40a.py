mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

import mystuff
mystuff.apple()
print mystuff.tangerine

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	def apple(self):
		print "I AM CLASSY APPLES!"
		
thing = MyStuff()
thing.apple()
print thing.tangerine

#dict style
mystuff['apples']

#module style
mystuff.apples()
print mystuff.tangerine

#class style
thing = MyStuff()
thing.apples()
print thing.tangerine