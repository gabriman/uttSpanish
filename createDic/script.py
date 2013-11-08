import string 

def codeNoum(code):
	p1="N/"
	
	#Analyze Gender
	if code[2]=='M':p2='Gp'
	elif code[2]=='F':p2='Gf'
	elif code[2]=='C':p2='Gn'

	#Analyze Number
	p3='N'+code[3].lower()

	return p1+p2+p3


def codeVerb(code):
	p1="V/"
	
	#Analyze Type TY
	p2='TY'+code[1].lower()

	#Analyze Mode M
	if   code[2]=='I':p3='Md'
	elif code[2]=='S':p3='Ms'
	elif code[2]=='M':p3='Mi'
	elif code[2]=='N':p3='Mb'
	elif code[2]=='G':p3='Mg'
	elif code[2]=='P':p3='Mp'

	#Analyze Time T 
	if   code[3]=='P':p4='Tr'
	elif code[3]=='I':p4='Ti'
	elif code[3]=='F':p4='Tf'
	elif code[3]=='S':p4='Tp'
	elif code[3]=='C':p4='Tc'
	elif code[3]=='0':p4=''

	#Analyze Person
	p5='P'+code[4]

	#Analyze Number
	p6='N'+code[5].lower()

	#Analyze Gender
	if code[6]=='M':p7='Gp'
	if code[6]=='F':p7='Gf'
	else: p7=''

	return p1+p2+p3+p4+p5+p6+p7


def codeAdj(code):
	p1="ADJ/"
	
	#Analyze Type T
	if   code[1]=='Q':p2='Tq'
	elif code[1]=='O':p2='To'
	else: p3=''

	#Analyze Degree D
	if code[2]=='C':  p3='Dc'
	elif code[2]=='A':p3='Da'
	elif code[2]=='D':p3='Dd'
	elif code[2]=='S':p3='Ds'
	else: p3=''

	#Analyze Gender G
	if   code[3]=='M':p4='Gp'
	elif code[3]=='F':p4='Gf'
	elif code[3]=='C':p4='Gc'
	else: p4=''

	#Analyze Number N
	if   code[4]=='S':p5='Ns'
	elif code[4]=='P':p5='Np'
	elif code[4]=='N':p5='Nn'
	else: p5=''

	#Analyze Function F
	if code[5]=='P':p6='Fp'
	else: p6=''

	return p1+p2+p3+p4+p5+p6

def codeAdv(code):
	p1="ADV/"
	
	#Analyze Type T
	if   code[1]=='G':p2='Tg'
	elif code[1]=='N':p2='Tn'
	else: p2=''

	return p1+p2


def codeDet(code):
	p1="D/"
	
	#Analyze Type T
	if   code[1]=='D':p2='Td'
	elif code[1]=='P':p2='Tp'
	elif code[1]=='T':p2='Tt'
	elif code[1]=='E':p2='Te'
	elif code[1]=='I':p2='Ti'
	elif code[1]=='A':p2='Ta'
	else: p2=''

	#Analyze Person
	p3='P'+code[2]

	#Analyze Gender G
	if   code[3]=='M':p4='Gp'
	elif code[3]=='F':p4='Gf'
	elif code[3]=='C':p4='Gc'
	elif code[3]=='N':p4='Gn'
	else: p4=''

	#Analyze Number N
	if   code[4]=='S':p5='Ns'
	elif code[4]=='P':p5='Np'
	elif code[4]=='N':p5='Nn'
	else: p5=''

	#Analyze Owner
	if   code[5]=='S':p6='Os'
	elif code[5]=='P':p6='Op'
	else: p6=''

	return p1+p2+p3+p4+p5+p6



def codePro(code):
	p1="PRO/"
	
	#Analyze Type T
	if   code[1]=='P':p2='Tp'
	elif code[1]=='D':p2='Td'
	elif code[1]=='X':p2='Tx'
	elif code[1]=='I':p2='Ti'
	elif code[1]=='T':p2='Tt'
	elif code[1]=='R':p2='Tr'
	elif code[1]=='E':p2='Te'
	else: p2=''

	#Analyze Person
	p3='P'+code[2]

	#Analyze Gender G
	if   code[3]=='M':p4='Gp'
	elif code[3]=='F':p4='Gf'
	elif code[3]=='C':p4='Gc'
	elif code[3]=='N':p4='Gn'
	else: p4=''

	#Analyze Number N
	if   code[4]=='S':p5='Ns'
	elif code[4]=='P':p5='Np'
	elif code[4]=='N':p5='Nn'
	else: p5=''

	#Analyze Case C
	if   code[5]=='N':p6='Cn'
	elif code[5]=='A':p6='Ca'
	elif code[5]=='D':p6='Cd'
	elif code[5]=='O':p6='Co'
	else: p6=''

	#Analyze Owner O
	if   code[6]=='S':p7='Os'
	elif code[6]=='P':p7='Op'
	else: p7=''

	#Analyze Polite POL
	if code[7]=='P':p8='POLp'
	else: p8=''

	return p1+p2+p3+p4+p5+p6+p7+p8


def codeConj(code):
	p1="CONJ/"
	
	#Analyze Type T
	if   code[1]=='C':p2='Tc'
	elif code[1]=='S':p2='Ts'
	else: p2=''

	return p1+p2


def codeInt(code):
	p1="I"

	return p1


def codeConj(code):
	p1="CONJ/"
	
	#Analyze Type T
	if   code[1]=='C':p2='Tc'
	elif code[1]=='S':p2='Ts'
	else: p2=''

	return p1+p2


def codePrep(code):
	p1="P/"
	
	#Analyze Type T
	p2='Tp'

	#Analyze Form F
	if   code[2]=='S':p3='Fs'
	elif code[2]=='F':p3='Ff'
	else: p3=''

	#Analyze Gender G
	if   code[3]=='M':p4='Gp'
	elif code[3]=='F':p4='Gf'
	else: p4=''

	#Analyze Number N
	if   code[4]=='S':p5='Ns'
	elif code[4]=='P':p5='Np'
	else: p5=''

	return p1+p2+p3+p4+p5


def  compareBase(word, base):
	index=0;
	while index < len(word): 
		if (index<len(base)) and (word[index] == base[index]):
			index=index+1
			continue
		codeInt=len(word)-index
		code=str(codeInt)+base[index::]

		return code
	return 0


# MAIN

f = open ("nuevoDicc.txt", "w")

for line in file('dicc8.src'):

	splited = line.split()

	for block in range(len(splited)/2):

		code = splited[2*(block+1)]

		if code[0]=='N':
			nuevo=codeNoum(code)

		elif code[0]=='V':
			nuevo=codeVerb(code)

		elif code[0]=='A':
			nuevo=codeAdj(code)

		elif code[0]=='R':
			nuevo=codeAdv(code)

		elif code[0]=='D':
			nuevo=codeDet(code)

		elif code[0]=='P':
			nuevo=codePro(code)

		elif code[0]=='C':
			nuevo=codeConj(code)

		elif code[0]=='I':
			nuevo=codeInt(code)

		elif code[0]=='S':
			nuevo=codePrep(code)




		f.write(splited[0]+";"+str(compareBase(splited[0],splited[2*block+1]))+","+nuevo+"\n")
	
    # line contiene la linea actual

f.close()
		



