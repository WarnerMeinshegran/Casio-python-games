d=KeyError
c=ValueError
V='1'
U=len
Q=False
N=input
I=print
B=int
A=True
import math
from random import choice as Z
import random
W=['dad','toy','tug','can','boy','car','fat','tax','bat','sip','pie','bit','form','gaze','milk','boat','miss','sack','part','unit','head','cook','moan','gate','stop','rest','drop','aunt','jail','iron','sofa','grab','look','dogs','sock','fire','melt','dirt','soup','pain','wine','film','bolt','worm','self','frog','rule','slip','blow','wall','thaw','bell','seed','fall','lick','cave','reply','laugh','carve','sense','shelf','smell','month','store','cloth','crook','cover','juice','kneel','death','shape','skirt','chase','plant','found','order','cause','scent','metal','smile','noise','shrug','mourn','spoon','place','limit','chalk','trade','rescue','inform','animal','polish','wobble','sneeze','pencil','advice','reject','wonder','remind','employ','attack','memory','wander','bucket','spring','winter','invent','escape','porter','poison','hammer','reason','health','expert','chance','liquid','bridge','arrange','partner','receipt','command','radiate','kittens','quality','support','suggest','concern','cabbage','cushion','imagine','fiction','station','country','undress','applaud','stretch','disgust','fireman','holiday','purpose','manager','complain','birthday','stocking','building','chickens','reaction','memorize','friction','existence','knowledge','influence']
e='WORD PREDICT!\nLevel:{0} Pts:{3}\nPts req to lvl{1}:{2}\n1.Start a new game\n2.Settings\n\nOPTION NUMBER:'
f='SETTINGS|0 to quit\n1.Show first letter: \n{0}\n2.Show last letter: \n{1}\n3.Next page\nOPTION NUMBER:'
g='SETTINGS|0 to quit\n1.Guess tries:{0}\n2.gradual difficulty:\n{1}\n3.Credits&Save\n4.Load save\nOPTION NUMBER:'
h='Credits\nDeveloper:\nblabla_lab\nVersion:1.2\nSave code:\n{1}\nWords:{0}\nPRESS EXE'
def D(text):I('\n');I(text);N('PRESS EXE')
def X(x):
	if x:return Q
	else:return A
J=A
K=Q
E=6
F=0
O=2
G=0
H=A
Y=3
def i():
	M=','
	try:L=str(N('Save code:\n'));P=L.split(M)[0:1];C=list(L.split(M)[1]);I(C)
	except c:D('Only numbers in\nsave code, but I\nfound something thats\nnot a number')
	global F,G,E,H,J,K,O;F=B(P[0]);G=B(C[0]);E=B(C[1]);H=A if C[2]==V else Q;J=A if C[3]==V else Q;K=A if C[4]==V else Q;O=B(L.split(M)[2]);I('load save');I(F,G,E,H,J,K,O)
R=E
Y=3+G
def j(do_prompt=Q):
	C=1 if H is A else 0;I=1 if J is A else 0;L=1 if K is A else 0;B='{0},{1}{2}{3}{4}{5},{6}'.format(F,G,E,C,I,L,O)
	if do_prompt:D('{0}\nwrite this in a paper'.format(B))
	else:return B
while A:
	try:
		C=B(N(e.format(B(G),B(B(G)+1),B(O)-B(F),B(F))))
		if C==2:
			while A:
				C=B(N(f.format(J,K)))
				if C==0:raise d()
				elif C==1:J=X(J)
				elif C==2:K=X(K)
				elif C==3:
					C=B(N(g.format(E,H)))
					if C==1:
						E=B(N('\n\nGuessing Tries\n(default:6,min:1,\nmax:9):\n\n'))
						if E>9:D('You set\nGuessing Tries\nto more than 9\n\n\n')
						elif E<=0:D('You set\nGuessing Tries\nto less than 1\n\n\n')
						else:R=E
					elif C==2:H=X(H)
					elif C==3:N(h.format(U(W),j()))
					elif C==4:
						try:i()
						except IndexError:D('Wrong save code')
					elif C==0:continue
	except c:D('Only Numbers!');continue
	except d:continue
	a=Q
	if F>=O:G+=1;O+=math.ceil(G*1.3+F);Y+=1
	if not H:P=Z(W)
	elif H is A:
		while A:
			P=Z(W)
			if U(P)<=Y:break
			else:continue
	R=E;L=[]
	for T in P:L.append(T)
	S=[];b=[]
	for T in L:S.append('_')
	if J:S[0]=L[0]
	if K:S[-1]=L[-1]
	while A:
		if a:break
		I(P);I('Points:{0} Tries:{2}\nLevel:{1}\nPress 1 to exit\n'.format(F,G,R));I(''.join(S));M=str(N('Guess a letter:\n')).lower()
		if M==V:D('YOU QUITED!\nThe word was\n{}\n\n'.format(P));break
		elif U(M)>1:D('Only one letter')
		elif M.isdigit():D('type a word,\nnot a digit!')
		if M in L:
			k=[A for A in range(U(L))if L[A]==M]
			for T in k:S[T]=M
			if S==L:D('YOU DID IT!\nThe word was\n{}\n\n'.format(P));a=A;F+=1;break
		else:
			I('WRONG')
			if R<=0:D('YOU LOSE!\nThe word was\n{}\n\n'.format(P));break
			elif not R<=0 and not M in b:R-=1;b.append(M)
