AX='Play a card'
AW='give device\nto {}'
AV='CPU {}'
AU='Added player:\n{}'
AT='Wild Card'
AS='Draw 2 Green'
AR='9 Green'
AQ='8 Green'
AP='7 Green'
AO='6 Green'
AN='5 Green'
AM='4 Green'
AL='3 Green'
AK='2 Green'
AJ='1 Green'
AI='Draw 2 Blue'
AH='9 Blue'
AG='8 Blue'
AF='7 Blue'
AE='6 Blue'
AD='5 Blue'
AC='4 Blue'
AB='3 Blue'
AA='2 Blue'
A9='1 Blue'
A8='Draw 2 Red'
A7='Draw 2 Yellow'
A6='9 Yellow'
A5='8 Yellow'
A4='7 Yellow'
A3='6 Yellow'
A2='5 Yellow'
A1='4 Yellow'
A0='3 Yellow'
z='2 Yellow'
y='1 Yellow'
x=range
l='The placed card is {}'
k='2'
j='Draw 2'
i=print
d='Wild'
c='no'
b='1'
a=ValueError
Z=len
U='Draw 4'
R='Green'
Q='Blue'
P='Red'
O='Yellow'
N=','
M='CPU'
J=input
G=False
F=True
from random import choice as I
import String_methodes as A
m='UnoTerminal'
AY='1.0Mini'
AZ=[y,z,A0,A1,A2,A3,A4,A5,A6,A7,'Wild Yellow','Skip Yellow','Draw 4 Yellow']
Aa=['1 Red','2 Red','3 Red','4 Red','5 Red','6 Red','7 Red','8 Red','9 Red',A8,'Wild Red','Skip Red','Draw 4 Red']
Ab=[A9,AA,AB,AC,AD,AE,AF,AG,AH,AI,'Wild Blue','Skip Blue','Draw 4 Blue']
Ac=[AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,'Wild Green','Skip Green','Draw 4 Green']
n=[y,z,A0,A1,A2,A3,A4,A5,A6]
o=['1 Red','2 Red','3 Red','4 Red','5 Red','6 Red','7 Red','8 Red','9 Red']
p=[A9,AA,AB,AC,AD,AE,AF,AG,AH]
q=[AJ,AK,AL,AM,AN,AO,AP,AQ,AR]
r=[A7,A8,AI,AS,U,AT]
Ad=AZ+Aa+Ab+Ac
e=n+o+p+q
V=4
H=[]
f=1
S=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Ae='{Name}!\n1-Play\n2-Settings\n3-Players\n0-Quit\n--Type a number--\n'.format(Name=m)
Af='Settings|0 to quit\n1-Cards per player:\n{Cards_per_player}\n2-Credits\n--Type a number--\n'
Ag="Whats the name\nof the player you\nwant to add?\nseperate names by ','\nto batch add names\n-(1:cancel)-\n"
Ah='Manage players\n1.Add \n2.Back \n3.Remove\n4.View players \n5.Add bot\n'
Ai='Credits\n{Name} {Version}\nMade by blabla_lab\nThanks for playing\n'.format(Name=m,Version=AY)
def s(name,check_comma=F):
	D='Player not added. Name contained unallowed letters.';B=name
	if Z(B)>9 or Z(B)<=0:A.warn('Player name too long/short. max. plr name: 9 letters and min.1 letter');return G
	if B.find(M)!=-1:A.warn('You cant use the name CPU, its reserved for bots')
	try:H.index(B)
	except a:pass
	else:A.warn('name is duplicate');return G
	if check_comma:
		for C in list(B):
			if C not in S:A.warn(D);return G
	else:
		S.append(N)
		for C in list(B):
			if C not in S:A.warn(D);S.remove(N);return G
		S.remove(N)
def L(amount,player,silent=G):
	E=silent;C=amount;B=player
	if B.find(M)!=-1:D=F
	else:D=G
	for H in x(C):
		J=I(e+r)
		if not E and not D:A.warn('Card {0} out of {1}\n{3} got {2}\n'.format(H+1,C,J,B))
		elif D and not E:A.warn('{} drew {}/{} card(s)\n'.format(B,H+1,C),clear_screen=G)
		K[B].append(J)
def t(card):
	global g;K[D].remove(card)
	if K[D]==[]:A.warn('The winner is {}'.format(D));g=F
def u():
	B=' '
	if E==AT:return F
	elif E.startswith(j):
		A=C.split(B)[1]
		if E.endswith(O)and A==O:return F
		elif E.endswith(P)and A==P:return F
		elif E.endswith(Q)and A==Q:return F
		elif E.endswith(R)and A==R:return F
	D=E.split(B)[0];H=E.split(B)[1];I=C.split(B)[0];A=C.split(B)[1]
	if D==I:return F
	elif H==A:return F
	elif D=='Draw'and H=='4':return F
	else:return G
def W(card):
	B=card
	if B.find(O)!=-1:return I(n)
	elif B.find(P)!=-1:return I(o)
	elif B.find(Q)!=-1:return I(p)
	elif B.find(R)!=-1:return I(q)
	else:A.warn('Error occurred while replacing magic card\nchoose random card');return I(e)
def Aj(player):
	H.remove(player)
	if B.find(M)==-1:A.warn('Removed player:\n{}'.format(B))
	else:A.warn('Removed bot:\n{}'.format(B));C-=1
while F:
	A.clr_scrn();B=J(Ae)
	if B=='0':break
	elif B==k:
		A.clr_scrn();B=J(Af.format(Cards_per_player=V))
		if B=='0':continue
		elif B==k:A.clr_scrn();B=J(Ai)
		elif B==b:
			A.clr_scrn()
			try:
				B=int(J('a to cancel\nCards per player:\n'))
				if B<4 or B>15:raise a
				if B=='a':continue
			except a:A.warn('Type a number between 4 and 15');continue
			else:V=B
	elif B=='3':
		A.clr_scrn();B=J(Ah.format(A.add_line_breaks(N.join(H))))
		if B==b:
			A.clr_scrn();B=J(Ag)
			if B==b:continue
			if B.find(N)!=-1:
				for v in B.split(N):
					if s(v)is G:continue
					else:H.append(B);A.warn(AU.format(v))
			elif s(B)is G:continue
			else:H.append(B);A.warn(AU.format(B))
		elif B==k:continue
		elif B=='3':
			A.clr_scrn();B=A.view_list(H,title='-Remove player-')
			try:H.index(B)
			except a:A.warn('Player not found')
			else:Aj(B)
			finally:continue
		elif B=='4':A.clr_scrn();A.view_list(H,readonly=F,title='--Players--')
		elif B=='5':H.append(AV.format(f));A.warn('Added bot:\n{} !'.format(AV.format(f)));f+=1
		continue
	if B!=b:continue
	elif Z(H)<2:A.warn('Need at least 2 players to start game.');continue
	A.clr_scrn();i('Preparing cards...');K={}
	for X in H:K[X]=[I(e+r)for A in x(V)]
	Am=None;A.clr_scrn()
	for D in H:
		while F:
			if D.find(M)==-1:
				J(AW.format(D))
				if A.ask('Are you {}?\n'.format(D),['yes',c],prompt=G)==c:continue
				A.warn('click exe to view your cards,NEVER show your cards!'.format(D));A.view_list(K[D],readonly=F,title='--Cards--')
			else:A.warn('{} has saw its cards\npress exe to continue'.format(D))
			break
	while F:
		global C;C=I(Ad)
		if C.startswith(j)or C.startswith(U)or C.startswith(d)or C.startswith('Skip'):continue
		else:break
	w=[]
	for X in H:
		if X.find(M)==-1:w.append(X)
	g=G
	while g is G:
		for D in H:
			T=F if D.find(M)!=-1 else G
			if T is G and Z(w)!=1:
				J(AW.format(D))
				if A.ask('Are you {}?'.format(D),['yes',c])==c:continue
			else:0
			if C.startswith(j):A.warn(l.format(C));L(2,D);C=W(C)
			elif C.startswith(U):A.warn(l.format(C));L(4,D);C=W(C)
			elif C.startswith('Skip'):
				if not T:A.warn('YOU ARE SKIPPED')
				elif T:A.warn('{} is skipped'.format())
				C=W(C)
			elif C.startswith(d):C=W(C)
			if not T:B=A.ask(l.format(C),['Draw a card',AX],prompt=G)
			elif T:
				i(A.add_line_breaks('The placed card is {}. {} is thinking...'.format(C,D)));Ak=K[D];h=0
				while F:
					try:E=Ak[h]
					except IndexError:L(1,D,F);break
					Y=u()
					if Y is G:
						if h>V:L(1,D,F);break
						h+=1;continue
					if Y:
						i(A.add_line_breaks('{} played {}'.format(D,E)));t(E)
						if E.startswith(U):E='Draw 4 {}'.format(I([P,R,Q,O]))
						elif E.startswith(d):E='Wild {}'.format(I([P,R,Q,O]))
						C=E;break
				J('{} is done\n'.format(D));continue
			if B==AX:
				E=A.view_list(K[D],pick_confirm_question='Play {}?',title='placed card:{}'.format(C));Y=u()
				if Y:
					t(E)
					if E.startswith(d)or E.startswith(U):Al=A.ask('pick a color for {}'.format(E),[P,Q,R,O],prompt=G);C='{0} {1}'.format(E,Al)
					else:C=E
					continue
				else:J('You cant play this\ncard! You will\ndraw a card');L(1,D);continue
			else:A.warn('Press EXE to DRAW a card');L(1,D)
