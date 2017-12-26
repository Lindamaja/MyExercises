from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		#be sure to print out the last scene
		current_scene.enter()
		
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have incaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Amory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot":
			print "Quick on the draw you yank out your blaster and fire it at the gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him enitrely. That"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you reapetedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'
			
		elif action == "dodge":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothom stomps on"
			print "your head and eats you."
			return 'death'
			
		elif action == "tell a joke":
			print "Luckz for you thez made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe ygure sk daj dfkj, sdju ekjhua aijwq lskoi aje ojs os le hwui, asdjioa lciuh hausdh"
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't stop."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
			
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory, there is the neutron bomb."
		print "There is a keypad lock on the box. If your get the code whong 10 times"
		print " the lock closes forever and you can't get the bomb."
		print "The code is three digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 10:
			print "BZZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "The container opens"
			print "You run with the bomb to the bridge"
			return 'the_bridge'
		else:
			print "The lock buzzes one las time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You die."
			return 'death'
			
			
			
class TheBridge(Scene):

	def enter(self):
		print "When you get to the bridge there are 5 Gothons, that havent"
		print "pulled their weapons yet, because they dont want to set of the bomb"
	
		action == raw_input("> ")
	
		if action == "throw the bomb":
			print "You throw it and run for the door, but as you drop it"
			print "a Gothon shoots you right in the back killing you"
			return 'death'
		
		elif action == "slowly place the bomb":
			print "You back off with you blaster pointed at the bomb"
			print "You place the bomb once you've gotten to the door"
			print "punch the close button and blast the lock."
			print "Now you run to the escape pod"
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"
		
		
class EscapePod(Scene):

	def enter(self):
		print "When you get to the escape pods there is 5 of them."
		print "Which one do you take?"
		good_pod = randit(1,5)
		guess = raw_input("[pod #]> ")
		
		
		if int(guess) != good_pod:
			print "you jump into the pod %s and hit the eject button." % guess
			print "The pod implodes and you die."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject buttopn." % guess
			print "The pod slides into space towards the planet below."
			print "You won!"
			
			return 'finished'
			
class Finished(Scene):

	def enter(self):
		print " You won! Good Job!!"
		return 'finished'
		
class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()