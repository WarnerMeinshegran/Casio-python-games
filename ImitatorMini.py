_E='PASS THE DEVICE TO {}'
_D='Added player:\n{}'
_C='Imitator'
_B=True
_A=False
from random import choice as choose,randint
from String_methodes import*
NAME=_C
VERSION=1.3
CREATION_DATE='30/May/2023'
ANIMALS={'Dog':'A loyal animal, often a pet.','Cat':'An independent animal, often a pet.','Horse':'A large and powerful animal used for transportation.','Cow':'A large and docile animal, used for milk and meat.','Chicken':'A small and social animal, used for eggs and meat.','Fish':'A cold-blooded vertebrate that lives in water.','Bird':'A warm-blooded vertebrate that has feathers and wings.','Elephant':'The largest land animal on Earth.','Giraffe':'The tallest land animal on Earth.','Lion':'A large, powerful animal, the king of the jungle.','Tiger':"A large, striped animal. it's the same as Lion",'Bear':'A large, furry mammal that can be found in North America, Europe, and Asia.','Monkey':'A small, furry mammal that has a long tail and lives in trees.','Dolphin':'A marine mammal, related to whales and porpoises.','Shark':'A large, predatory fish that has sharp teeth.','Octopus':'A marine creature with eight arms and a beak.','Snail':'A creature with a soft body and a shell. it is slow','Bee':'An insect that makes honey.','Ant':'An insect that lives in colonies and works together to gather food.','Grasshopper':'An insect that jumps and eats plants.','Cockroach':'An insect, often considered a pest.','Spider':'An arthropod with eight legs.','Scorpion':'An arthropod with a long, thin body and a stinger.','Snake':'A long, legless reptile that has scales.','Lizard':'A reptile with a long tail and scales.','Turtle':'A reptile with a hard shell that protects its body.','Chameleon':'A lizard that can change its color to blend in with its surroundings.','Jellyfish':'A marine creature with a bell-shaped body and tentacles.','Whale':'A large, marine mammal, the largest animal on Earth.'}
OBJECTS={'chair':'A piece of furniture with four legs and a seat.','table':'A piece of furniture with a flat top and legs.','computer':'A device that is used to process information.','phone':'A device that is used to make and receive calls.','book':'A collection of written or printed pages.','pen':'A writing instrument with a pointed tip.','pencil':'A writing instrument with a flat tip.','eraser':'A tool used to remove marks from paper.','ruler':'A tool used to measure distances.','marker':'A tool used to write on a board.','hat':'A covering for the head.','shirt':'A piece of clothing worn on the upper body.','pants':'A covering for the lower body.','umbrella':'A covering used to protect from rain or sun.','watch':'A device that tells time.','phone case':'A case for a phone.','ball':'A toy that is round and bounces.','glove':'A piece of clothing worn on the hands.'}
def check_name(name,check_comma=_B):
	A='Player not added. Name contained unallowed letters.'
	if len(name)>9 or len(name)<=0:warn('Player name too long/ too short. max. 9 letters and min.1 letter');return _A
	try:players.index(name)
	except ValueError:pass
	else:warn('name is duplicate');return _A
	if check_comma:
		for i in list(name):
			if i not in PLAYER_NAME_ALLOWED_LETTERS:warn(A);return _A
	else:
		PLAYER_NAME_ALLOWED_LETTERS.append(',')
		for i in list(name):
			if i not in PLAYER_NAME_ALLOWED_LETTERS:warn(A);PLAYER_NAME_ALLOWED_LETTERS.remove(',');return _A
		PLAYER_NAME_ALLOWED_LETTERS.remove(',')
no_of_questions=5
players=[]
PLAYER_NAME_ALLOWED_LETTERS=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
MAIN_MENU='{0}\n1.Play\n2.Players\n----0:Quit----\n'.format(NAME)
PLAYERS_MENU='Plrs:{0}\n-1.add 2.back 3.rmv\n4.all plrs-\n'
ADD_PLAYER_MENU="Whats the name\nof the player you\nwant to add?\nseperate names by ','\nto batch add names\n-(1:cancel)-\n"
ROLE_MENU='{0}\nYou are an:\n{1}.\n{2}\ndont tell anyone!\npress exe to continue'
QUESTION_MENU='Questions({0}/{1})\nHey {2},\nask {3}.\nwhen done press EXE'
invalid=_A
while _B:
	vote=[];clr_scrn();user_input=int(input(MAIN_MENU))
	if user_input==0:clr_scrn();raise SystemExit('Quit')
	elif user_input==2:
		while _B:
			clr_scrn();user_input=int(input(PLAYERS_MENU.format('\n'.join(players))))
			if user_input==2 or user_input is None:break
			elif user_input==4:clr_scrn();warn('\n'.join(players),_A)
			elif user_input==3:
				clr_scrn();user_input=ask('type the index of the player to remove',players)
				if user_input=='1':warn('Player name not\nremoved.\nPress EXE',_A);continue
				players.remove(user_input);warn('removed player:\n{}'.format(user_input))
			elif user_input==1:
				clr_scrn();new_player_name=input(ADD_PLAYER_MENU).strip().replace('  ',' ')
				if new_player_name=='1'or user_input is None:warn('Player name not\nadded.\nPress EXE',_A);continue
				if new_player_name=='1qa':new_player_name='DumOne,DumTwo,DumThree'
				if new_player_name.find(','):
					for i in new_player_name.split(','):
						if check_name(i,_A)is _A:warn('operation stopped');break
						else:players.append(i);warn(_D.format(i))
					continue
				elif check_name(new_player_name)is _A:continue
				players.append(new_player_name);warn(_D.format(new_player_name));new_player_name=None
	elif user_input==1:
		quit_game=_A
		if len(players)<=2:warn('not enough players');continue
		catagory=randint(1,2)
		if catagory==1:idea=choose(list(ANIMALS.keys()));definition=ANIMALS[idea]
		elif catagory==2:idea=choose(list(OBJECTS.keys()));definition=OBJECTS[idea]
		Imitator=choose(players)
		if catagory==1:idea_hint='a animal'
		elif catagory==2:idea_hint='a food'
		elif catagory==3:idea_hint='a object'
		no_of_questions=int(input(add_line_breaks('How many questions do you want in this round?(def: 5)')))
		for i in range(0,len(players)):
			warn(_E.format(players[i]))
			while _B:
				if not ask('PRESS 1 TO CONFIRM YOU ARE {}'.format(players[i]),['Im {}'.format(players[i]),'Im not {}'.format(players[i])],prompt=_A)=='Im {}'.format(players[i]):continue
				else:break
			warn(ROLE_MENU.format(players[i],_C if Imitator==players[i]else'Innocent','idea is {idea}:'.format(idea=idea)if Imitator!=players[i]else'Try to guess idea'),_A)
			if Imitator==players[i]:warn('Goodluck, try to ask questions that help identify idea\nalso the idea is {hint}'.format(hint=idea_hint))
			else:warn('definition of {0}:{1}'.format(idea,definition),auto_break_lines_every=20)
		warn('Pass the device to someone to announce who to ask whom.');prev_asker_player=''
		for i in range(0,no_of_questions):
			while _B:
				asker=choose(players);answerer=choose(players)
				if asker==answerer:continue
				if asker==prev_asker_player:continue
				else:prev_asker_player=asker;break
			if warn(QUESTION_MENU.format(i,no_of_questions,asker,answerer),_A)=='1':quit_game=_B;break
		for i in range(0,len(players)):
			if quit_game:break
			warn(_E.format(players[i]));vote.append(ask('Who is imitating to\nunderstand the speech\nsubject?',players,_A))
		try:warn('Time to reveal the\nimitator...\npress EXE to reveal',_A);warn('The most voted player\nas imitator:\n{0}\nThe imitator was:\n{1}'.format(max(set(vote),key=vote.count),Imitator),_A)
		except ValueError:warn('The game was quit by the admin')
		warn('Game finished')
