#William Aguirre Zapata grass.py
#Funcion solve(L,H,a) modificado por el algoritmo hecho en clase
from sys import stdin
from operator import itemgetter
import math

def solve(L,H,a):
    ans,low,n,ok,N = 0,L,0,True,len(a)
    while ok and low<H and n!=N:
        ok = a[n][0]<=low
        best,n = n,n+1
        while ok and n!=N and a[n][0]<=low:
            if a[n][1]>a[best][1]:
                best = n
            n += 1
        ans+=1
        low = a[best][1]
    ok = ok and low>=H
    if ok==False:
        ans = -1
    return ans

def main():
    global spr
    linea = stdin.readline()
    while len(linea) != 0:
        n, l, w = map(int, linea.split())
        spr=[]
        for i in range(n):
            x,r = map(int, stdin.readline().split())
            if r*2 > w:
                dx = math.sqrt((r*r) - ((w*w)/4))
                spr.append((x-dx,x+dx))
        spr = sorted(spr, key = lambda x: (x[0],x[1]))
        print(solve(0,l,spr))
        linea = stdin.readline()

main()