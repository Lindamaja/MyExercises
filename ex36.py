from sys import exit

def cottage():
	print "The cottage is quite dirty, but no one is home."
	print "What do you do? \na) leave again (who lives in this mess?!) \nb) clean up and cook something delicious, because why not"
	
	choice = raw_input("> ")
	
	if "a" in choice:
		dead("You could've let the huntsman kill you, would have been faster, Snow White..")
	elif "b" in choice:
		dwarfs()
	else:
		cottage("Choose 'a' or 'b', this isn't too hard")


def dwarfs():
	print "After cooking and cleaning you are tired and fall asleep."
	print "The bed is really uncomfortable and quite small"
	print "You wake up to seven dwarfs staring at you"
	print "How do you react? \na) scream and run \b) offer them the food you made and tell your story"
	
	
	choice = raw_input("> ")
	
	if "a" in choice:
		dead("The dwarfs are insulted and send you back into the forest where you die slowly, Snow White..")
	elif "b" in choice:
		knocking()
	else:
		dwarfs("Choose 'a' or 'b', this isn't too hard")
		
def knocking():
	print "The drawrf take you in and let you live with them."
	print "You work for them as a maid, but at least you live."
	print "Seven 'grown' dwarfs can be messy though.."
	print "One day it knocks on the door while the dwarfs are off to work."
	print "Do you open the door ('open') or ignore the knocking ('ignore')"
	
	choice = raw_input("> ")
	
	if "open" in choice:
		apple()
	elif "irgnore" in choice:
		print "You live happily ever after with seven drawrfs in a tiny cottage, congrats!"
		exit(0)
	else:
		knocking("You gotta do something..")
			
def apple():
	print "You open the door and a darling old lady offers you apples."
	print "She has a basket full of apples and offers you a shiny red one"
	print "Do you eat it? yes or no"
	
	choice = raw_input("> ")
	
	if "yes" in choice:
		print "The apple was poisoned, nasty old witch."
		print "You fall into a coma, but at least you're not dead. Congrats!"
		exit(0)
	elif "no" in choice:
		print "You live happily ever after with seven drawrfs in a tiny cottage, congrats!"
		exit(0)
	else:
		choice_b("Type yes or no, this isn't too hard.")
	
			
def dead(why):
	print why, "Game over"
	exit(0)
			
def choice_b():
	print "The huntsman has mercy on you and lets you go."
	print "You have no idea where you are."
	print "After stumbling through the forest all night you find a tiny cottage"
	print "Do you go inside? yes or no"
	
	choice = raw_input("> ")
	
	if "yes" in choice:
		cottage()
	elif "no" in choice:
		dead("You could've let the huntsman kill you, would have been faster, snow white..")
	else:
		choice_b("Type yes or no, this isn't too hard.")
	
	
def dead(why):
	print why, "Game over!"
	exit(0)
	
def start():
	print "You are in your room, brushing your black hair when someone breaks in through the window."
	print "A man jumps in and knocks you out."
	print "You wake up in a forest to him lifting a knife to cut your throat. What do you do?"
	print "Do you \na) scream and try to fight him or \nb) look at him, pleading with your best glance"
	
	choice = raw_input("> ")
	
	if choice == "a":
		dead("The huntsman kills Snow White.")
	elif choice == "b":
		choice_b()
	else:
		dead("You kind of cover your beautiful face and the huntsman kills Snow White.")
		


start()