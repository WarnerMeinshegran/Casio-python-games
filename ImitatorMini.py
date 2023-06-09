y='Im {}'
x='PASS THE DEVICE TO {}'
w='Added player:\n{}'
v='learn more'
u='Imitator'
l='1'
k='no'
j=int
e='yes'
d=range
c=TypeError
X=''
W=list
V=input
U=print
Q=','
P=ValueError
L=None
K=len
I='\n'
G=True
D=False
from random import randint as z,choice as M
m=u
A0=1.3
AB='30/May/2023'
n={'Dog':'A loyal animal, often a pet.','Cat':'An independent animal, often a pet.','Horse':'A large and powerful animal used for transportation.','Cow':'A large and docile animal, used for milk and meat.','Chicken':'A small and social animal, used for eggs and meat.','Fish':'A cold-blooded vertebrate that lives in water.','Bird':'A warm-blooded vertebrate that has feathers and wings.','Elephant':'The largest land animal on Earth.','Giraffe':'The tallest land animal on Earth.','Lion':'A large, powerful animal, the king of the jungle.','Tiger':"A large, striped animal. it's the same as Lion",'Bear':'A large, furry mammal that can be found in North America, Europe, and Asia.','Monkey':'A small, furry mammal that has a long tail and lives in trees.','Dolphin':'A marine mammal, related to whales and porpoises.','Shark':'A large, predatory fish that has sharp teeth.','Octopus':'A marine creature with eight arms and a beak.','Snail':'A creature with a soft body and a shell. it is slow','Bee':'An insect that makes honey.','Ant':'An insect that lives in colonies and works together to gather food.','Grasshopper':'An insect that jumps and eats plants.','Cockroach':'An insect, often considered a pest.','Spider':'An arthropod with eight legs.','Scorpion':'An arthropod with a long, thin body and a stinger.','Snake':'A long, legless reptile that has scales.','Lizard':'A reptile with a long tail and scales.','Turtle':'A reptile with a hard shell that protects its body.','Chameleon':'A lizard that can change its color to blend in with its surroundings.','Jellyfish':'A marine creature with a bell-shaped body and tentacles.','Whale':'A large, marine mammal, the largest animal on Earth.'}
o={'Pizza':'flatbread topped with tomato sauce and other toppings.','Pasta':'type of noodle, often served with sauces.','Burger':'sandwich but rounded, with meat','Fried chicken':'Chicken, coated in a batter or breading and then fried.','Steak':'A cut of beef, grilled or pan-fried.','French fries':'deep-fried potato fingers.','Broast':'dish made of fried chicken and fried potato.','Salad':'dish of cut vegetables.','Soup':'liquid dish, often made with vegetables','Sandwich':'Two pieces of bread with toppings.','Tacos':'Mexican dish made with a corn tortilla','Burritos':'Mexican dish made with a flour tortilla','Sushi':'Japanese dish made with ricem and fish.'}
p={'chair':'A piece of furniture with four legs and a seat.','table':'A piece of furniture with a flat top and legs.','computer':'A device that is used to process information.','phone':'A device that is used to make and receive calls.','book':'A collection of written or printed pages.','pen':'A writing instrument with a pointed tip.','pencil':'A writing instrument with a flat tip.','eraser':'A tool used to remove marks from paper.','ruler':'A tool used to measure distances.','marker':'A tool used to write on a board.','hat':'A covering for the head.','shirt':'A piece of clothing worn on the upper body.','pants':'A covering for the lower body.','umbrella':'A covering used to protect from rain or sun.','watch':'A device that tells time.','phone case':'A case for a phone.','ball':'A toy that is round and bounces.','glove':'A piece of clothing worn on the hands.'}
def F():U(I*7)
def A1(x):
	try:j(x)
	except(P,c):return
	else:return j(x)
def A2(x):
	try:str(x)
	except(P,c):return
	else:return str(x)
def Y(message):
	while G:
		A=V(message)
		if A is L or A.strip()==X:U('Please enter a number');F();continue
		return A1(A)
def A3(message):
	while G:
		A=V(message)
		if A is L or A.strip()==X:U('Please enter text');F();continue
		return A2(A)
def q(string,every=20):
	A=string;A=A.strip();B=X
	for C in d(K(A)):
		if C%every==0:B+=I if A[C]in[' ','.',Q]else'-\n'
		B+=A[C]
	D=I.join(B.strip().split(I)).strip();E=[A.strip()for A in D.split(I)];return I.join(E)
def A(message,auto_break_lines=G,auto_break_lines_every=20):
	A=message;F()
	if auto_break_lines:B=V(q(A,auto_break_lines_every))
	else:B=V(A)
	F();return B
def R(question,ans=L,auto_break_lines=G,auto_break_lines_every=20,prompt=G):
	D=question;B=ans
	if B is L:B=[e,k]
	while G:
		if prompt:A('{question}\n\npress exe'.format(question=D),auto_break_lines,auto_break_lines_every)
		else:U(q(D))
		U('-',end=X)
		try:C=j(V('{}\n'.format('\n-'.join(B))))
		except(P,c):continue
		try:C-=1
		except c:continue
		if C<0:continue
		F()
		try:return B[C]
		except IndexError:continue
def r(name,check_comma=G):
	F='Player not added. Name contained unallowed letters.';C=name
	if K(C)>9 or K(C)<=0:A('Player name too long/ too short. max. 9 letters and min.1 letter');return D
	try:B.index(C)
	except P:pass
	else:A('name is duplicate');return D
	if check_comma:
		for E in W(C):
			if E not in S:A(F);return D
	else:
		S.append(Q)
		for E in W(C):
			if E not in S:A(F);S.remove(Q);return D
		S.remove(Q)
Z=5
N=G
B=[]
S=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
A4='{0}\n1.Play\n2.Players\n3.Settings\n----0:Quit----\n'.format(m)
A5='Plrs:{0}\n-1.add 2.back 3.rmv\n4.all plrs-\n'
A6='Settings\n1.No. questions: {0}\n2.Credits\n3.Imitator assist:\n{1}\n----(0:cancel)----\n'
A7="Whats the name\nof the player you\nwant to add?\nseperate names by ','\nto batch add names\n-(1:cancel)-\n"
AD='{}\nName of plr to rmv:\n-(1:cancel)-\n'
A8='{0}\nYou are an:\n{1}.\n{2}\ndont tell anyone!\npress exe to continue'
A9='Questions({0}/{1})\nHey {2},\nask {3}.\nwhen done press EXE'
AE="Hey {0},\nwho's imitating?\n{1}"
AA='Credits\n{game_name} {version}\nby blabla_lab (H.A)\nThanks for playing.\n'.format(game_name=m,version=A0)
AF=D
while G:
	f=[];F();C=Y(A4)
	if C==0:F();raise SystemExit('Quit')
	if C==3:
		F();C=Y(A6.format(Z,N))
		if C==1:
			F()
			try:C=Y('No. of questions to be asked:')
			except P:continue
			if C<0 or C>50:continue
			Z=C
		elif C==2:F();A(AA,D)
		elif C==3:
			g=R('Turn on imitator assist to make the game easier?',[e,k,v],prompt=D)
			if g==e:N=G
			elif g==k:N=D
			elif g==v:A('Easier for imitator: tell type of idea, not first answerer when more than 3 players.')
	elif C==2:
		while G:
			F();C=Y(A5.format(I.join(B)))
			if C==2 or C is L:break
			elif C==4:F();A(I.join(B),D)
			elif C==3:
				F();C=R('type the index of the player to remove',B)
				if C==l:A('Player name not\nremoved.\nPress EXE',D);continue
				B.remove(C);A('removed player:\n{}'.format(C))
			elif C==1:
				F();H=A3(A7).strip().replace('  ',' ')
				if H==l or C is L:A('Player name not\nadded.\nPress EXE',D);continue
				if H=='1qa':H='DumOne,DumTwo,DumThree'
				if H.find(Q):
					for E in H.split(Q):
						if r(E,D)is D:A('operation stopped');break
						else:B.append(E);A(w.format(E))
					continue
				elif r(H)is D:continue
				B.append(H);A(w.format(H));H=L
	elif C==1:
		s=D
		if K(B)<=2:A('not enough players');continue
		O=z(1,3)
		if O==1:J=M(W(n.keys()));h=n[J]
		elif O==2:J=M(W(o.keys()));h=o[J]
		elif O==3:J=M(W(p.keys()));h=p[J]
		T=M(B);a='Sorry, but I \ncant help you'
		if N:
			if O==1:a='a animal'
			elif O==2:a='a food'
			elif O==3:a='a object'
		for E in d(0,K(B)):
			A(x.format(B[E]))
			while G:
				if not R('PRESS 1 TO CONFIRM YOU ARE {}'.format(B[E]),[y.format(B[E]),'Im not {}'.format(B[E])],prompt=D)==y.format(B[E]):continue
				else:break
			A(A8.format(B[E],u if T==B[E]else'Innocent','idea is {idea}:'.format(idea=J)if T!=B[E]else'Try to guess idea'),D)
			if T==B[E]:
				if N:A('Goodluck, try to ask questions that help identify idea\nalso the idea is {hint}'.format(hint=a))
				else:A('Goodluck, try to ask questions that help identify idea')
			else:A('definition of {0}:{1}'.format(J,h),auto_break_lines_every=20)
		A('Pass the device to someone to announce who to ask whom.');t=X
		for E in d(0,Z):
			while G:
				b=M(B);i=M(B)
				if b==i:continue
				if N:
					if E==0 and K(B)>=4:
						if i==T:continue
				if b==t:continue
				else:t=b;break
			if A(A9.format(E,Z,b,i),D)==l:
				if R('You pressed 1\n\nQuit game?',prompt=D)==e:s=G;break
				else:continue
		for E in d(0,K(B)):
			if s:break
			A(x.format(B[E]));f.append(R('Who is imitating to\nunderstand the speech\nsubject?',B,D))
		try:A('Time to reveal the\nimitator...\npress EXE to reveal',D);A('The most voted player\nas imitator:\n{0}\nThe imitator was:\n{1}'.format(max(set(f),key=f.count),T),D)
		except P:A('The game was quit by the admin')
		A('Game finished')
