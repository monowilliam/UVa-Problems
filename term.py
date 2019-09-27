#William Aguirre Zapata term.py
from sys import stdin

INF = float('inf')

L,E,memo,a=[],0,[],0

def termMemo(asig,e):
	if asig==a:
		return 0
	if e<=0:
		return -INF
	if memo[asig][e] != -1:
		return memo[asig][e]
	i=0
	ans=-INF
	while i<E and i+1 <= e:
		if L[asig][i] >=5:
			ans = max(ans, termMemo(asig + 1, e-(i + 1)) + L[asig][i])
		i+=1
	memo[asig][e] = ans
	return ans

def main():
	tcnt = int(stdin.readline())
	global L,E,memo,a
	while tcnt != 0:
		L=[]
		memo=[ [ -1 for c in range(121) ] for k in range(111) ]
		dim = stdin.readline().split()
		a=int(dim[0])
		e=E=h=int(dim[1])
		for i in range(a):
			fila = list(map(int, stdin.readline().split()))
			L.append(fila)
		ans = termMemo(0,e)/a
		if ans<5:
			print("Peter, you shouldn't have played billiard that much.")
		else:
			a="{0:.2f}".format(ans)
			print(f'{"Maximal possible average mark - "}{a}{"."}')
		tcnt -= 1
main()