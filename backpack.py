#William Aguirre Zapata backpack.py
from sys import stdin

millas=[]

def verificar(nCamp,nNoches,mid):
	i,j,tmp,ans=0,0,0,None
	while i != nCamp and j <= nNoches:
		if millas[i]+tmp <= mid:
			tmp+=millas[i]
			i+=1
			ans=True
		else:
			tmp=0
			j+=1
			ans=False
	return ans

def busquedaBinaria(nCamp,nNoches):
	low,hi = 0,sum(millas)
	while low+1 != hi:
		mid = low + ((hi-low)>>1)
		if verificar(nCamp,nNoches,mid):
			hi = mid
		else:
			low = mid
	return hi

def main():
	global millas
	dupla = stdin.readline()
	while len(dupla) != 0:
		a=dupla.split()
		nCamp,nNoches,millas = int(a[0]),int(a[1]),[]
		for i in range(nCamp+1):
			millas.append(int(stdin.readline()))
		print(busquedaBinaria(nCamp+1,nNoches))
		dupla = stdin.readline()

main()