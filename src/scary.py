# Creator: Luis Felipe Rojas


import time
# import time for time.sleep()
answer = ""
command = ""
#These will be the primary ways of getting user input
satchel = []
#This is our bag/inventory
note = 0
#One of the key items to help the user one
medical_kit = 0
#Most important item. User CANNOT win without it
hp = 50
reply = ""



#defining hp function
def health_points(x,hp):
	hp += x
	if command == "hp" or answer == "hp":
		print("(You have", hp, "hp)")
	return x,hp
	 
	
#defining satchel
def open_satchel(satchel):
	if len(satchel) != 0:
		print("Inventory:", satchel)
	elif len(satchel) == 0:
		print("Your satchel is empty!!!")
	else:
		print("Invalid Command!")
	return satchel




#defining adding itmes to satchel with max items being 3
def add_item(note, medical_kit, satchel):
	while 1==1:
		print("What item would you like to add?")
		command = input()
		if command == "note" and len(satchel) <= 3:
			satchel.append("note")
			note += 1
			print("You added a note to your satchel!!!")
			break
			#This branch notes to be added to the satchel
		elif len(satchel) > 3:
			print("Your bag is full!!!")
			break
			#sets bag limit
		else:
			print("invalid command!")
			continue
			#prevents user from saying random commands
	return note, medical_kit, satchel



def remove_item (note, medical_kit, satchel):
	while 1==1:
		print("What item would you like to remove?")
		command = input()
		if command == "medical kit" and "medical kit" in satchel:
			print("You remove a medical kit")
			satchel.remove("medical kit")
			medical_kit -= 1
			#These branches allow the user to remove notes or the medical kit. It will only be used once if the user wants to remove the medical kit, which is a key part of the adventure
		else:
			print("Invalid command!")
			continue
			#prevents random commds
		return note, medical_kit, satchel




#define area titiled honey's room
def honeys_room():
	print("You slowly push the door open, and the sharp creaking of the old and rotting wood sends shivers down your spine. You feel around for a light switch, and find one. However, after flicking it up and down multiple times, nothing happens. You decide that it would be best to use the perimenter of the room to guide you because it is far too dark to see.")
	hp = 60
	#setting hp to 60 because user starts with 50, but they find a bandage to increase it to 60 before honeys_room was called.
	while 1==1:	
		print("Do you want to proceed to the (left) or the (right)?")
		answer = input()
		if answer == "open satchel":
			print(open_satchel(satchel))
			continue
		elif answer == "hp":
			print("You have", hp, "hp!")
			continue
		#The two branches above allow for the user to open their satchel or check hp
		elif answer == "right":
			print("You slowly make your way down the wall, hoping to find more bandages for your wound that is progressively getting worse. After some feeling around. You come across a nightstand that has a lamp on it. You feel a knob on the lamp and rotate it. The lamp illuminates the room. Within the blink of an eye you are mauled by a giant wolf that pounces on you from the middle of the room and suffer a slow death as it eats you alive...\n\n GAME OVER!")
			quit()
			#This branch ends the game, forcing the user to proceed left.
		elif answer == "left" or answer == "beeline for the door" or answer == "turn off the flashlight":
			print("\n\nYou slowly make your way down the wall, hoping to find any more bandages for your wound that is progressively getting worse. After some feeling around, you bump into a small table. Upon sweeping your hand on the surface of the table, there seems to be nothing. However, you reach lower and find a drawer attached to the table. Inside the drawer you find another bandage(+10 hp) battery, and a medical kit (a medical kit restores your health fully... use it wisely). The battery turns out to be a perfect match for the flashlight.") 
			x,hp = health_points(10,60)
			satchel.append("medical kit")	
			break
			#This branch adds 10 hp and adds the medical kit to the satchel.
			
	print("Next to the battery was a crumpled up piece of paper. You turn the flashlight on and uncrumple the paper. There is a message on the inside that reads: 'You so carelessly did not listen to my warning. Oh well, I guess you will have to play my little game. Since you are off to a bad start, let me offer you a little hint. Honey prefers the dark...' Awfully confused, you add the note to your satchel, as you still don't know why you are here or who it is that put you here. You try not to give the note much thought and carry on. As you turn around, it is still relatively dark because the flashlight is not very powerful. As you slowly scan the room, you notice an object obstructing the light. You slowly scan across the object because it is difficult to make out. You continue to move the light over the obejct until you reach the end of it, and suddenly a sharp, yellow glare comes to life. An intense shock rushes through your body. As you begin to make out what the object is, an enormous wolf that was sleeping in the middle of the room comes to life and towers over your body. A gowl muffled in slobber bellows. You glance at the door and need to make a quick decision.")
	satchel.append("note")
	#Note is added to the satchel, and this text box forces the user into one of two options.
	if answer == "left":
		while 1==1:
			print("Do you (beeline for the door) or (turn off the flashlight)?")
			answer = input()
			if answer == "beeline for the door":
				print("You sprint towards the door, while continuing to shine your light at the exit in order to make your way. The wolf, Honey, is drawn toward the light and eventually claws at you. As you tremble and fall in agony, Honey dismembers you limb by limb, and you perish :( \n\n GAME OVER!")
				quit()
			elif answer == "turn off the flashlight":
				print("\n\nYou think back to the note and decide to take a long-shot. You turn off your flashlight and brace yourself. Suddenly, the room goes quiet. There is a slight echoe of muffled huffing that stems from the center of the room. However, the breathing slowly becomes more faint. Because you remember the general direction of the door, you make your way back along the wall until you find it. You then slowly exit and shut the door behind you. That was a close one :)")
				print("While still in shock, you do your best to maintain your composure. After a few minutes, you finally stare down the dark hallway. There is nowehere else for you to go, so you make your way...")
				break
				#user input determines whether or not they end the game again. The user will hopefully use the hint from the note to assume that you will turn the flashlight off instead of running with it on.
			elif answer == "open satchel":
				print(open_satchel(satchel))
				continue
			elif answer == "hp":
				print("You have", hp, "hp!")
				health_points(0,70)
				continue
				#The two branches above allow the user to open their satchel or check their hp

#deinfe an area called tri_room

def tri_room():
	print("After few minutes of walking, you come to another area that is also being illuminate by a single light bulb. As you scan the room, you see three doors. They are each covering up different rooms that are blocked off by a giant wall.")
	hp = 70
	#setting hp = 70 to establish the local variable
	while 1==1:
		print(" Which door do you want to pick??? (left) (right) or (center)")
		answer = input()
		#the user is forced into one of three options. The only one that ends the game is "right"
		if answer == "left":
			print("You slowly turn the knob to the door and look inside. Nervous that there might be another man eating wolf inside this room, you flicker your flashlight. You get a glimpse of the room, and it looks fairly empty, so you turn on your flashlight. Upon scanning the room, you realize that there's nothing inside. Except, when you walk though the middle of the room, you notice another crumpled up note sitting in the dead center of the room. You grab the note, uncrumpple it, and read it. It says: 'I'm surprised you made it this far. If you use your flashlight that I have so graciously lended you, notice the buttom below.' You look and see that there is a red button right under where the note was. 'I have placed it there so that you may press it if you so choose. The choice is yours... You place the note in your satchel")	
			satchel.append("note")
			#note is added to the bag
			break
		if answer == "right":
			print("As you open the door, you hear the whisp of wind, which is very strange condidering there are no fans. You go to flicker your flashlight, so you don't accidentally awake any man eating wolves. Simultaneously, you take a sigle step into the room. You stumble, and loose balace as you realize there is no floor under you. You immediately plumet and land in ice cold water. As you shiver, you feel something slice you leg. As you look down to see what it was, you turn on your flaslight only to see a school of flesh devouring piranhas pursue you. You scream in agony as they begin to visciously eat you alive... :(\n\n GAME OVER!!!")
			quit()
			#User will end the program if this option is selected
		if answer == "center":
			print("You go to open the center door but it is locked........... You then hear a the sound of voice in the room to the left. You decide to investigate... You slowly turn the knob to the door and look inside. Nervous that there might be another man eating wolf inside this room, you flicker your flashlight. You get a glimpse of the room, and it looks fairly empty, so you turn on your flashlight. Upon scanning the room, you realize that there's nothing inside. Except, when you walk though the middle of the room, you notice another crumpled up note sitting in the dead center of the room. You grab the note, uncrumpple it, and read it. It says: 'I'm surprised you made it this far. If you use your flashlight that I have so graciously lended you, notice the buttom below.' You look and see that there is a red button right under where the note was. 'I have placed it there so that you may press it if you so choose. The choice is yours... You place the note in your satchel")	
			satchel.append("note")
			break
			#This answer leads to essentially the same outcome as if the user were to say "left". The note is added to the satchel here too
		elif answer == "open satchel":
			print(open_satchel(satchel))
			continue
		elif answer == "hp":
			print("You have", hp, "hp!")
			continue
			#The two branches above allow the user to open their satchel or check their hp


	while 1==1:
		print("Do you want to press the button or not??? (yes) or (no)")
		answer = input()
		#The user is forced into another game ending decision. If they say "yes", they conitnue. If they say "no", they die
		if answer == "yes":
			print("You place the note in your satchel and push the button... There is a rumble that sounds like it came from one of the other rooms. You decide to go check it out. You try to open the middle room, but it is locked. Therefore, it must be the rightmost room. Again, you slowly open the door to the room, and you flicker your lights. You see that all is normal, and you walk to the center of the room. There is a table with another note. The note says: 'You are lucky to have made it to this point. Not many do... Hopefully your luck continues You want to add the note to your bag, but you have reached your three item limit. Would you like to exchange the note for your medical kit?")
			break
			
		#user is forced into leaving a note for their medical kit or keeping the medical kit. This is the move that decided whether or not the user has a chance to win. If they keep the medical kit and makethe correct decisions the rest of the way, they win. If they take the note instead of the medical kit, they will never win. The input for the decision is received on line 193
		if answer == "no":
			print("You hesistate and decide that you shouldn't because it may end badly. Slightly panicked you swiftly head towards the door. When you turn the knob, it gives slightly, but a clciking sound occurs and locks the door. You try to turn it again, but somehow, the knob is scorching hot, and your hand gets burned and starts blistering. The temperature quickly rises in the room. As your heart races, you run to press the button. You press it, but nothing happens. The room is still getting hotter, and anytime, you touch the walls or door, you get burned. You try hard to think of a way to escape, but eventually, the heat gets to you, and you collapse. The heat continues to increase, and you are slowly cooked to death :(\n\n Game Over!!!")
			quit()
		elif answer == "open satchel":
			print(open_satchel(satchel))
			continue
		elif answer == "hp":
			print("You have", hp, "hp!")
			continue
			#The two branches above allow the user to open their satchel or check their hp


	while 1==1:		
		print("(yes) or (no)")
		answer = input()
		#user chooses to keep medical kit or not
		if answer == "yes":
			remove_item(note, medical_kit, satchel)
			add_item(note, medical_kit, satchel)
			#the user has to remove the kit and add the note themselves via the add_item and remove_item functions
			print("You exchange the medical kit for the note and leave the room...")
			break
		if answer == "no":
			print("You keep the medical kit and leave the room...")
			break
			#The user doesn't know it, but they are on the right path to win
		elif answer == "open satchel":
			print(open_satchel(satchel))
			continue
		elif answer == "hp":
			print("You have", hp, "hp!")
			health_points(0,70)	
			continue
			#The two branches above allow the user to open their satchel or check their hp

#The final room is being defined and called later om
def makers_room():
	print("Upon exiting the room, you hear a creaking sound. You look over and see that the door to the center room is wide open. It is too dark to see, so you have no choice but to enter. You walk inside. Before you can flicker your flashlight, the door behind you slams shut. You try the knob and it won't budge. Lights then illuminate the room. However, this isn't even a room. It is a small, narrow hall, reinforced with cold, metal walls. There is also a large metal door in front of you. The door has a key pad. A speaker behind you sounds, and a man with a distored voice says 'This is the last trial, figure out the five letter code to the keypad, and you are free. However, you only have one chance. Good luck.....' Your heart skips a beat, but you are unsure of what the word would be. You think and realize that the only way you could possibly come up with an answer is through the notes. You uncrumple them, and after satring at them for a while. You realize that they look like they were torn from the same piece of paper.\n\n")
	#Here the user with three notes is likely thinking they've won, but they are wrong. I give the user with two notes enough to hopefully get them to figure it out below. (They may not notice, but it says their HEART skipped a beat above hehe)
	while 1==1:	
		if "medical kit" not in satchel:
			time.sleep(2) 
			print("You line up the three notes and it seems that the inside portion of the paper that was used to write the notes is cut out to form a heart with jagged edges. What will you type into the keypad??? (Answer MUST be in all CAPS!!!")
			answer = input()
			#The user most likely will enter the right code, as I literally gave it to them, but they will die no matter what.
			if answer == "HEART":
				print("A lound rumble ensues, and the door unlocks. Smoke seeps through the door, and a bright light shines...\n\n An old man wearing a white button up and black dress slacks approaches you. He says: 'well done, you've made it. You've earned a second chance at life... He then draws a pistol and shoots you in the stomach (-50 hp)... You bleed to death as he stands over you. Two people in hazmat suits pick you up as you fade away. One of them says: 'Why do they always fail right at the end?' As they carry you away, you notice a symbol on their chests. It is a heart with jagged edges.....\n\n You fall uncosncious and slowly bleed away the rest of your hp....")
				print("\n\n\n GAME OVER!!!!!")
				quit()
			elif answer == "open satchel":
				print(open_satchel(satchel))
				continue
			elif answer == "hp":
				hp = 70
				print("You have", hp, "hp!")	
				continue
				#The two branches above allow the user to open their satchel or check their hp
			if answer != "HEART":
				print(answer, " was not the correct code. A green gass seeps into the room through air vents at the top, and you slowly choke on the gas until you die. \n\n GAME OVER!!!!")
				quit()

		if "medical kit" in satchel:
			time.sleep(2)
			print("You only have two of the notes. You still try putting them next to one another, and it looks as if the two pieces form a 'V' shape with jagged edges. The point of the 'V' is at the bottom, and it looks like the third note was torn from the top of the paper. You only have one chance to guess. (Answer Must be in all CAPS!!!!)")
			answer = input()
			#this is the game deciding branch. If the user can figure out the code, they win
			if answer == "HEART":
				print("A lound rumble ensues, and the door unlocks. Smoke seeps through the door, and a bright light shines...\n\n An old man wearing a white button up and black dress slacks approaches you. He says: 'well done, you've made it. You've earned a second chance at life... He then draws a pistol and shoots you in the stomach (-50 hp)...\n\n As you struggle for breath, your reach into your bag and grab your medical kit. Although you try to apply first aid, you are too weak. Two people in hazmat suits pick you up as you fade away. They apply the medical kit for you (+80 hp). One of them says: 'congrats kid, you made it. Don't worry, we'll patch you up.")
				x,hp = health_points(-50,70)
				x,hp = health_points(80,20)
				print("Your hp has been fully resotered to 100!\n\n")
				time.sleep(2) 
				print("After they patch you up, one of the people says: 'Hang in there kid. You can't quit now. You're just getting started. You're movin' on to the AWAKENING.' The other person says: 'QUIET, are you trying to get us in touble??' Your eyes slowly move around and see that there are poeple in lab coats eevrywhere, and a woman on a large screen appears and says: 'Subject 211-A successfully completed the Slaughter trial' You look up and notice a symbol on the wall. It is a HEART with jagged edges.")
				#defining function for ascii art
				heart = (""" 	
						_░▒███████
						░██▓▒░░▒▓██
						██▓▒░__░▒▓██___██████
						██▓▒░____░▓███▓__░▒▓██
						██▓▒░___░▓██▓_____░▒▓██
						██▓▒░_______________░▒▓██
						_██▓▒░______________░▒▓██
						__██▓▒░____________░▒▓██
						___██▓▒░__________░▒▓██
					q	____██▓▒░________░▒▓██
						_____██▓▒░_____░▒▓██
						______██▓▒░__░▒▓██
						_______█▓▒░░▒▓██
						_________░▒▓██
						_______░▒▓██
						_____░▒▓██
				""")
				print(heart)
				time.sleep(4)
				print("You are overwhelmed, hoping everything is just a dream, and drift away..............................................\n\n\n YOU WON......this trial at least...")
				quit()
				#Here the user has successfully entered the code and been restored to full hp. They win the game :)
			elif answer == "open satchel":
				print(open_satchel(satchel))
				continue
			elif answer == "hp":
				hp = 70
				print("You have", hp, "hp!")	
				continue
				#The two branches above allow the user to open their satchel or check their hp
			if answer != "HEART":
				print(answer, " was not the correct code. A green gass seeps into the room through air vents at the top, and you slowly choke on the gas until you die. \n\n GAME OVER!!!!")
				quit()
				#The user has made given an incorrect answer and loses at the very end :(


#introduction and name establishment
while 1==1:
	print("Hello user. This is a game that will send you on a perilous journey, in which you may not return. Do you wish to continue??? (Yes/No)\n")
	answer = input()
	if answer == "Yes":
		print("Very well.")
		break
	elif answer == "No":
		print("You have made a wise choice. Farewell...\n""Game Over!")
		quit()
#User has begun the game and the user will be forced into one of two areas:
while 1==1:
	print("Before embarking on your journey, I would like to know your name...")
	name = input()
	print("I see... Well,", name, "allow me to welcome you to hell on Earth...")
	time.sleep(3)
	break
	#getting the users name to make the game feel more personalized

print("\n\nYou wake up on the a damp and sticky hardwood floor. There is a single lightbulb hanging over your head, which is barely illuminating the room. You look down only to find your white t-shirt soaked in blood. Because of how disoriented you are, a delayed rush of pain comes on, and you lift up your shirt and see a large gash that seems to be slowly leaking blood. In a panic, you look around the room to find an exit, help, or even first-aid. Ahead of you, there is a hallway and a door that seems to be open slightly.")
while 1==1:
	print("Will you (peer inside the room), or (walk down the hallway)?")
	answer = input()
	if answer == "peer inside the room" or answer == "walk down the hallway":
		print("\n\nRight when you make your way, you stumble over something. Because you are not standing directly under the lightbulb, it is hard to see, so you bend over to feel what it is you've tripped over. The item appears to be a satchel. (Note: This satchel is your inventory and it can hold three items. You can also open the satchel to see your inventory by saying 'open satchel') As you look through the satchel, you notice that there is a single bandage inside as well as a flashlight. (Note: you have health points (hp), and you can check your hp by at any time by saying 'hp'. A bandage adds +10 hp. You are currently at 50 out of 100 hp due to your wounds!) In a hurry, you patch your wound as best as you can (+10 hp), but the one bandage won't last long. The flashlight also has no batteries inside, but you decide to wield it as a weapon for now. You remember that your were going to", answer, " It's not too late to change your mind", name)
		x,hp = health_points(10,50)
		break 
		#The user goes through the introductory phase. Depending on their answer here, they may or may not embark on the rest of their journey
while 1==1:	
	print("... Do you want to (go inside the room) or (walk through the hallway)?")
	answer = input()
	if answer == "go inside the room":
		#The user chose correctly and triggers all of the functions that allow them to embrak on the main portion of the game
		print("You", answer)
		honeys_room()
		tri_room()
		makers_room()
		break
	elif answer == "walk through the hallway":
		print("You walk through the hallway, and halfway through, lights turn on and illuminate the entire hallway. You look up and see a bee fly out of a vent. The bee is followed, by another, and then thousands more start coming out through vents that line the entire hallway. They chase you and sting you over and over until you fall to the ground. You are stung to death as you lie in a pile of dead bees, while more swarm you.\n\n GAME OVER!!!")
		break
		#They lose the game right away if they choose this option
	elif answer == "open satchel":
		print(open_satchel(satchel))
		continue
	elif answer == "hp":
		health_points(0,60)	
		continue
		#The two branches above allow the user to open their satchel or check their hp


