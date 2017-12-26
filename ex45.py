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
		


class Starting(Scene):

	def enter(self):
		print "You wake up with a pounding head in an unknown room that slowly starts to "
		print "becomes apparent through dark spots in your sight. You try to remember where "
		print "you are... \n"
		print "After a while a memory starts to shape: Last night you were in a Casino with your "
		print "friend Jules, making easy money by counting cards. Seems like the money came too "
		print "easily and the managers security separated you two and carried you into some room."
		print "Before they knocked you out, you heard Jules' sceams somehwere down the hall."
		print "They told you that only if you are able to get out"
		print "They will let Jules go, if not you are apparently not as smart as you thought you were."
		print "Three objects catch your interest. A lamp (a), a painting (b) and a suitcase (c)."
		print "Which one do you take a closer look at?"
		
		action = raw_input("> ")
		
		if action == "a":
			return 'object_lamp'
			
		elif action == "b":
			return 'object_painting'
			
		elif action == "c":
			return 'object_suitcase'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'starting_point'
			
class Lamp(Scene):

	def enter(self):
		print "The lamp is old doesn't switch on. You investigate the cable and find out"
		print "It was not plugged in.. Duh! \n"
		print "Still doesn't switch on. You check the lightbulb and find it not twisted in enough."
		print "Now it switches on. Three letters are shown on the lampshade: W Y D ?"
		print "Seems like this doesn't lead anywhere. You move on to (b) the paining"
		print "or (c) the suitcase"
		
		choice = raw_input("> ")
	
		if "b" in choice:
			return 'object_painting'
		elif "c" in choice:
			return 'object_suitcase'
		else:
			return 'object_lamp' ("Choose 'b' or 'c', this isn't too hard")
			
class Painting(Scene):

	def enter(self):
		print "On the painting you see a scenery of an old farm with some"
		print "trees and fields. You take it off, look at it closely, but don't find "
		print "anything. Nothing is hidden in the paper, nor in the frane."
		print "Wrong choice. You move on to (a) the lamp"
		print "or (c) the suitcase"
		
		choice = raw_input("> ")
	
		if "a" in choice:
			return 'object_lamp'
		elif "c" in choice:
			return 'object_suitcase'
		else:
			return 'object_painting' ("Choose 'a' or 'c', this isn't too hard")
			
class Suitcase(Scene):

	def enter(self):
		print "The Suitcase is quite old and worn-out. There is a combination lock"
		print "prohibiting you from opening it. Above the lock someone wrote: "
		print "'WHAT IS THE SENSE OF LIFE?' in cricket letters. The lock has "
		print "two digits. Enter two."
		sense_of_life = '42'
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != sense_of_life and guesses < 4:
			print "Not correct, try again"
			guesses += 1
			guess = raw_input("[keypad]> ")
		
		if guess == sense_of_life:
			print "The suitcase opens"
			print "inside you find a lot of crumpled paper and........ a key!"
			return 'the_wardrobe'
			
		else:
			print "You will sit here forever..."
			print "Read 'The Hitchhiker's Guide to the Galaxy' and come back "
			print "once you know it."
			exit(1)
			
class Wardrobe(Scene):

	def enter(self):
		print "You open the wardrobe and find it is not only a wardrobe.."
		print "Behind some Jackets you see a doorknob"
		print "You grab it and it is - of course - locked. After going through the jackets"
		print "pockets, you find one that fits the lock. They made it pretty easy here."
		print "Wonder what is waiting behind that door..."
		return 'finished'

class Finished(Scene):
	def enter(self):
		print "Just a (so far) empty hallway.. onto the next adventure.."
		print "You won!! Good Job :-)"
		return 'finished'		
		

		
class Map(object):

	scenes = {
		'starting_point': Starting(),
		'object_lamp': Lamp(),
		'object_painting': Painting(),
		'object_suitcase': Suitcase(),
		'the_wardrobe': Wardrobe(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)		

		
a_map = Map('starting_point')
a_game = Engine(a_map)
a_game.play()