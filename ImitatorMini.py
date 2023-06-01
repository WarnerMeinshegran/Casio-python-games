m='pass the device to {}'
l='Added player:\n{}'
k='removed player:\n{}'
j='Spider'
i=TypeError
X='Imitator'
W=ValueError
U=list
T=range
S=print
P=int
L=len
K=True
J='\n'
I=','
H=input
E=False
from random import randint as n,choice as M
Y=X
o=1.
x='30/May/2023'
y='1/June/2023'
Z={'Dog':'A loyal animal, often a pet.','Cat':'An independent animal, often a pet.','Horse':'A large and powerful animal used for transportation.','Cow':'A large and docile animal, used for milk and meat.','Chicken':'A small and social animal, used for eggs and meat.','Fish':'A cold-blooded vertebrate that lives in water.','Bird':'A warm-blooded vertebrate that has feathers and wings.','Elephant':'The largest land animal on Earth.','Giraffe':'The tallest land animal on Earth.','Lion':'A large, powerful animal, the king of the jungle.','Tiger':"A large, striped animal. it's the same as Lion",'Bear':'A large, furry mammal that can be found in North America, Europe, and Asia.','Monkey':'A small, furry mammal that has a long tail and lives in trees.','Dolphin':'A marine mammal, related to whales and porpoises.','Shark':'A large, predatory fish that has sharp teeth.','Octopus':'A marine creature with eight arms and a beak.',j:'An arthropod with eight legs and a body divided into two parts.','Snail':'A creature with a soft body and a shell. it is slow','Bee':'An insect that makes honey.','Ant':'An insect that lives in colonies and works together to gather food.','Grasshopper':'An insect that jumps and eats plants.','Cockroach':'An insect, often considered a pest.',j:'An arthropod with eight legs.','Scorpion':'An arthropod with a long, thin body and a stinger.','Snake':'A long, legless reptile that has scales.','Lizard':'A reptile with a long tail and scales.','Turtle':'A reptile with a hard shell that protects its body.','Chameleon':'A lizard that can change its color to blend in with its surroundings.','Jellyfish':'A marine creature with a bell-shaped body and tentacles.','Whale':'A large, marine mammal, the largest animal on Earth.'}
z=[X,'Not Imitator']
a={'Pizza':'flatbread topped with tomato sauce and other toppings.','Pasta':'type of noodle, often served with sauces.','Burger':'sandwich but rounded, with meat','Fried chicken':'Chicken, coated in a batter or breading and then fried.','Steak':'A cut of beef, grilled or pan-fried.','French fries':'deep-fried potato fingers.','Broast':'dish made of fried chicken and fried potato.','Salad':'dish of cut vegetables.','Soup':'liquid dish, often made with vegetables','Sandwich':'Two pieces of bread with toppings.','Tacos':'Mexican dish made with a corn tortilla','Burritos':'Mexican dish made with a flour tortilla','Sushi':'Japanese dish made with ricem and fish.'}
def F():S(J*7)
def b(string,every=20):
	A=string;A=A.strip();C=''
	for B in T(L(A)):
		if B%every==0:
			if A[B]==' 'or A[B]=='.'or A[B]==I:C+=J
			else:C+='-\n'
		C+=A[B]
	E=J.join(C.strip().split(J)).strip();D=[]
	for B in E.split(J):D.append(B.strip())
	return J.join(D)
def A(message,auto_break_lines=K,auto_break_lines_every=20):
	A=message;F()
	if auto_break_lines:H(b(A,auto_break_lines_every))
	else:H(A)
	F()
def c(question,ans=['yes','no'],auto_break_lines=K,auto_break_lines_every=20):
	B=question
	while K:
		F()
		if auto_break_lines:S(b(B,auto_break_lines_every))
		else:S(B)
		S('-',end='')
		try:A=P(H('{}\n'.format('\n-'.join(ans))))
		except(W,i):continue
		try:A-=1
		except i:continue
		if A>=0:F();return ans[A]
		else:continue
def d(name,check_comma=K):
	F='Player not added. Name contained unallowed letters.';C=name
	if L(C)>10 or L(C)<=0:A('Player name too long/ too short');return E
	try:B.index(C)
	except W:pass
	else:A('name is duplicate');return E
	if check_comma:
		for D in U(C):
			if not D in N:A(F);return E
	else:
		N.append(I)
		for D in U(C):
			if not D in N:A(F);N.remove(I);return E
		N.remove(I)
Q=5
B=[]
N=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
p='{0}\n1.Add player\n2.Play\n3.Settings\n----0:Quit----\n'.format(Y)
q='Plrs:{0}\n-1.add 2.back 3.rmv-\n\n'
r='Settings\n1.No. questions: {0}\n2.Credits\n----(0:cancel)----\n'.format(Q)
s="Whats the name\nof the player you\nwant to add?\nseperate names by ','\nto batch add names\n-(1:cancel)-\n"
t='{}\nName of plr to rmv:\n-(1:cancel)-\n'
u='{0}\nYou are an:\n{1}.\n{2}\ndont tell anyone!\npress exe to continue'
v='Questions({0}/{1})\nHey {2},\nask {3}.\nwhen done press EXE'
A0="Hey {0},\nwho's imitating?\n{1}"
w='Credits\n{game_name} {version}\nby blabla_lab (H.A)\nThanks for playing.\n'.format(game_name=Y,version=o)
while K:
	V=[];A1=E;F();D=P(H(p))
	if D is E:continue
	if D==0:F();raise SystemExit('Quit')
	if D==3:
		D=P(H(r))
		if D==1:
			try:D=P(c('number of questions to ask:',['5','10','15','20']))
			except W:continue
			Q=D
		elif D==2:F();A(w,E)
	elif D==1:
		while K:
			F();D=P(H(q.format(J.join(B))))
			if D==2:break
			elif D==3:
				F();D=str(H(t.format(',\n'.join(B))))
				if D=='1':A('Player name not\nremoved.\nPress EXE',E);continue
				if D.find(I):
					for C in D.split(I):B.remove(C);A(k.format(C))
					continue
				else:B.remove(C);A(k.format(C))
			elif D==1:
				F();G=str(H(s)).strip().replace('  ',' ')
				if G=='1':A('Player name not\nadded.\nPress EXE',E);continue
				if G=='1qa':
					for C in['DumOne','DumTwo','DumThree']:B.append(C)
					continue
				if G.find(I):
					for C in G.split(I):
						if d(C,E)is E:A('operation stopped');break
						else:B.append(C);A(l.format(C))
					continue
				elif d(G)is E:continue
				B.append(G);A(l.format(G));G=None
	elif D==2:
		if L(B)<=2:A('Not enough players!');continue
		e=n(1,2)
		if e==1:O=M(U(Z.keys()));f=Z[O]
		elif e==2:O=M(U(a.keys()));f=a[O]
		R=M(B)
		for C in T(0,L(B)):
			A(m.format(B[C]));A(u.format(B[C],X if R==B[C]else'Innocent','idea is {}:'.format(O)if not R==B[C]else'Try to guess idea'),E)
			if R==B[C]:A('Goodluck, try to ask questions that help identify idea')
			else:A('definition of {0}:{1}'.format(O,f),auto_break_lines_every=20)
		for C in T(0,Q):
			while K:
				g=M(B);h=M(B)
				if g==h:continue
				A(v.format(C,Q,g,h),E);break
		for C in T(0,L(B)):A(m.format(B[C]));V.append(c('Who is imitating to\nunderstand the speech\nsubject?',B,E))
		A('Time to reveal the\nimitator...\npress EXE to reveal',E);A('The most voted player\nas imitator:\n{0}\nThe imitator was:\n{1}'.format(max(set(V),key=V.count),R),E);A('Game finished')