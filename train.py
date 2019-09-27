#William Aguirre Zapata train.py
from sys import stdin

def solve(Arr, lenArr):
    lis, lds, ans = [None for _ in range(lenArr) ],[None for _ in range(lenArr)],0
    for n in range(lenArr):
        lis[n] = lds[n] = 1
        for i in range(n):
            if (Arr[i]<=Arr[n] and lis[i]>=lis[n]):
                lis[n]=lis[i]+1
            if Arr[i]>=Arr[n] and lds[i]>=lds[n]:
                lds[n]=lds[i]+1
        ans = max(ans, lis[n]+lds[n]-1)
    return (ans)

def main():
    cpruebas = int(stdin.readline())
    carros, peso, pesos, lenPesos= 0,0,[],0
    while cpruebas != 0:
        carros = int(stdin.readline())
        while carros != 0:
            peso = int(stdin.readline())
            pesos.append(peso)
            carros -= 1
        cpruebas -= 1
        pesos.reverse()
        lenPesos = len(pesos)
        print(solve(pesos, lenPesos))
        pesos=[]

main()