#William Aguirre Zapata moliu.py
from sys import stdin

def solve(num):
    steps=0
    while num != 0:
        if (num % 2==0):
            num/=2
        else:
            if (((num-1)/2)%2 == 0) or (num-1==2):
                num-=1
            else:
                num+=1
        steps+=1
    return steps

def main():
    numero = stdin.readline()
    while len(numero) != 0:
        numero = int(numero)
        print(solve(numero))
        numero = stdin.readline()
main()