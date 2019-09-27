#William Aguirre Zapata problem.py
from sys import stdin

def solve(k):
  ans,n = 0,0
  if k < 0:
    k = k * -1
  n = int((k*2)**(1/2))
  if k%2 ==1:
    ans = int(n*(n+1))/2
    while ans < k or ans %2 == 0:
      n+=1
      ans = (n*(n+1))/2
  else:
    ans=int((n*(n+1))/2)
    while ans < k or ans %2 == 1:
      n+=1
      ans = (n*(n+1))/2
  if k == 0:
      n=3
  return n

def main():
  tcnt,first = int(stdin.readline()),True
  while tcnt!=0:
    stdin.readline()
    if first==False: print()
    first = False
    print(solve(int(stdin.readline())))
    tcnt -= 1

main()