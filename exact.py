#William Aguirre Zapata exact.py
#https://www.youtube.com/watch?v=Y0ZqKpToTic Me tocó guiarme en la idea del Coin Change
from sys import stdin

INF = float('inf')

def exact(D,pCompra,lenD,memo):
	i,bandera,memo[0]= 0, 0, 0
	while i<lenD:
		j=pCompra
		while j> -1:
			memo[D[i]+j] = min( memo[D[i]+j], memo[j]+1 )
			j-=1
		i+=1
	i=pCompra
	while i<=30000 and bandera == 0:
		if memo[i]<10000:
			montoT=i
			nDin=memo[i]
			bandera=1
		i+=1
	return montoT, nDin

def main():
	tcnt = int(stdin.readline())
	while tcnt !=0:
		pCompra = int(stdin.readline())
		lenD = int(stdin.readline())
		D=[]
		j=0
		for j in range(0, lenD):
			D.append(int(stdin.readline()))
		memo=[ INF for c in range(30000) ]
		montoT, nDin = exact(D,pCompra,lenD,memo)
		print(montoT, nDin)
		tcnt-=1

main()