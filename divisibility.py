#William Aguirre Zapata divisibility.py phi la funcion DP que el profesor nos dio en clase
from sys import stdin,setrecursionlimit
setrecursionlimit(11000)

N,K,num,dicc = None,None,None,None

def phi(A, N, K, k):
  ans = None
  if N==0: ans = (k==0)
  else:
    if (N,k) in dicc:
      ans = dicc.get((N,k))
    else:
      ans = phi(A, N-1, K, (k+A[N-1])%K) or phi(A, N-1, K, (k-A[N-1])%K)
      dicc[(N,k)] = ans
  return ans

def main():
  global N,K,num,dicc
  tcnt = int(stdin.readline())
  while tcnt!=0:
    dicc={}
    N,K = map(int, stdin.readline().split())
    num = list(map(int, stdin.readline().split()))
    print('Divisible' if phi(num, N, K, 0) else 'Not divisible')
    tcnt -= 1

main()
