J=len
I=input
F=True
D=print
from random import choice as P
K=['car','ray','mix','sip','rot','pie','boy','toy','sky','beg','can','tug','end','bit','tax','mom','fit','cow','dad','bat','two','day','sign','cook','mate','cork','wall','beer','ring','milk','mind','stir','step','thaw','long','fall','jail','glue','pain','sock','kick','meal','rake','hand','rain','coal','self','drop','dirt','worm','dogs','tale','name','chin','bell','hour','gate','grab','page','trip','live','form','last','carve','blade','allow','metal','noise','paper','girls','cloth','slave','offer','order','shape','reply','trade','smile','place','twist','employ','aspect','people','sneeze','winter','bucket','flower','spring','reason','degree','reduce','canvas','arrive','polish','cousin','advice','liquid','bottle','health','wander','trains','pencil','porter','invent','supply','receipt','undress','weather','suggest','stretch','trainer','pancake','purpose','library','support','fiction','history','applaud','morning','compete','develop','version','compare','country','cushion','writing','concern','manager','opinion','radiate','creator','partner','imagine','friction','creature','complain','accident','stranger','birthday','increase','instance','multiply','teaching','expansion','cigarette','knowledge','appliance','encourage','afternoon','existence','passenger','complaint','territory','selection','newspaper','president','committee','inspector','treatment','apparatus','statement','responsibility','transportation','administrative']
Q=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
R='WORD PREDICT!\n1.Play\n2.Credits\n3.Quit game\nOPTION NUMBER:'
S='Credits\nDeveloper:\nblabla_lab\nVersion:1.3\nWords:{0}'
def B(text):D('\n');D(text);I('PRESS EXE')
def X(x):return not x
T=F
U=F
L=6
G=L
while F:
	try:
		M=int(I(R))
		if M==3:break
		elif M==2:B(S.format(J(K)));continue
	except ValueError:B('Only Numbers!');continue
	except KeyError:continue
	N=False;H=P(K);G=L;C=list(H);O=[];E=['_'for A in C]
	if T:E[0]=C[0]
	if U:E[-1]=C[-1]
	while F:
		if N:break
		D('\n'*7);D('tries:{}\nPress 1 to quit game\n'.format(G));D(''.join(E));A=str(I('Guess a letter:\n')).lower()
		if A=='1':B('YOU QUITED!\nThe word was\n{word}\n\n'.format(word=H));break
		elif J(A)>1:B('Only one letter')
		elif A not in Q:B('You didnt type a letter!')
		if A in C:
			V=[B for B in range(J(C))if C[B]==A]
			for W in V:E[W]=A
			if E==C:B('YOU DID IT!\nThe word was\n{word}\n\n'.format(word=H));N=F;break
		else:
			D('WRONG')
			if G<=0:B('YOU LOSE!\nThe word was\n{word}\n\n'.format(word=H));break
			elif A not in O:G-=1;O.append(A)
