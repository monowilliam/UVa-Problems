#William Aguirre Zapata flight.py
from sys import stdin

INF = float('inf')
W,memo,x=[],[],0

def flight(a,m):
	if m==x and a==0:
		return 0
	if (a>9 or a<0 or m>x) or (m==x and a!=0):
		return INF
	if memo[a][m]: return memo[a][m]
	a1=flight(a-1,m+1)+60
	b1=flight(a,m+1)+30
	c1=flight(a+1,m+1)+20
	memo[a][m]=min(min(a1,b1),c1)-W[a][m]
	return memo[a][m]

def main():
	tcnt = int(stdin.readline())
	global W,memo,x
	while tcnt !=0:
		W=[]
		memo=[]
		x = stdin.readline()
		while x == '\n':
			x = stdin.readline()
		x = int(int(x)/100)
		for j in range(0,10):
			fila = list(map(int, stdin.readline().split()))
			W.append(fila)
		W.reverse()
		memo=[ [ None for c in range(x+1) ] for k in range(11) ]
		print(flight(0,0))
		print()
		tcnt-=1

main()