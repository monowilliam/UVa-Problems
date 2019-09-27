#William Aguirre Zapata cut.py
from sys import stdin

INF = float('inf')

A,memo=[],[]

def cut(a,b):
	i=a+1
	if memo[a][b] != INF:
		return memo[a][b]
	if i==b:
		return 0
	while i<b:
		memo[a][b] = min(memo[a][b], cut(a,i) + cut(i,b) + A[b]-A[a])
		i+=1
	return memo[a][b]

def main():
	global A, memo
	L = int(stdin.readline())
	while L != 0:
		A=[]
		A.append(0)
		ncortes = int(stdin.readline())
		A.extend(list(map(int, stdin.readline().split())))
		A.append(L)
		memo=[ [ INF for c in range(L) ] for k in range(L) ]
		ans= cut(0,ncortes+1)
		print(f'{"The minimum cutting is "}{ans}{"."}')
		L = int(stdin.readline())

main()