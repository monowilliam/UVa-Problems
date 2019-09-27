#William Aguirre Zapata set.py
from sys import stdin
from operator import itemgetter

def solve(S,G):
    temp1,temp2=[],[]
    for i in range(len(S)):
        if G[i] >= S[i]:
            temp1.append([S[i],G[i]])
        else:
            temp2.append([S[i],G[i]])
    ord1=sorted(temp1, key=itemgetter(0))
    ord2=sorted(temp2, key=itemgetter(1),reverse=True)
    ord1.extend(ord2)
    x=ord1[0][0]
    y=x+ord1[0][1]
    for i in range(1,len(ord1)):
        x=ord1[i][0]+x
        if x>y:
            y = x + ord1[i][1]
        else:
            y = y + ord1[i][1]
    return y

def main():
    linea = stdin.readline()
    while len(linea) != 0:
        S,G= [],[]
        S = list(map(int, stdin.readline().split()))
        G = list(map(int, stdin.readline().split()))
        print(solve(S,G))
        linea = stdin.readline()

main()