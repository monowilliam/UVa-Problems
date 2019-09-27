#William Aguirre Zapata product.py
#https://www.youtube.com/watch?v=vtJvbRlHqTA&t=2s
#Main ayuda del monitor
from sys import stdin

INF = float('inf')

def MaxSubSeqProd(a):
	Max, Min, pmax, pmin = 1, 1, 1, 1
	ans = -INF
	for i in a:
		Max = max(pmax * i, pmin * i, i)
		Min = min(pmin * i, pmax * i, i)
		ans = max(ans, Max)
		pmax, pmin = Max, Min
	return ans


def main():
	i,line = 0,stdin.readlines()
	while i < len(line):
		token,a,tmp=True,list(),list()
		while i<len(line) and token:
			linee =line[i].strip()
			tmp = [int(x) for x in linee.split()]
			token =tmp[-1] != -999999
			for j in tmp:
				if j != -999999:
					a.append(j)
			i = i+1 if token else i
		print(MaxSubSeqProd(a))
		i+=1

main()