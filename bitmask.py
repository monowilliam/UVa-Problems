#William Aguirre Zapata bitmask.py
#Código discutido con Tania Obando
from sys import stdin

def solve(N,L,U):
	N, L, U = str(bin(N)[2:].zfill(32)), str(bin(L)[2:].zfill(32)), str(bin(U)[2:].zfill(32))
	ans, x = 0, ''
	ok1, ok2 = True, True
	for i in range(32):
		if N[i] == '0':
			if U[i] =='0' and ok1:
				x+='0'
			else:
				if L[i] =='0':
					ok2 = False
				x+='1'
		else:
			if L[i] =='1' and ok2:
				x+='1'
			else:
				if U[i] =='1':
					ok1 = False
				x+='0'
	ans = int(str(x),2)
	return ans

def main():
	linea = stdin.readline()
	while len(linea) != 0:
		N, L, U = map(int, linea.split())
		print(solve(N,L,U))
		linea = stdin.readline()

main()