#William Aguirre Zapata Steps.py
from sys import stdin

def busquedaBinaria(low,hi,dist):
  while(hi>low):
    mid = low + ((hi-low)>>1)
    if mid *(mid+1) >= dist:
      hi=mid
    else:
      low = mid+1
  left = hi*(hi+1)-dist
  hi *=2
  if left >= low and low != 0:
    hi=hi-1
  return hi

def solve(x, y):
  ans = 0
  dist = y-x
  sqrt = int((dist**(1/2))+1)
  ans = busquedaBinaria(0,sqrt,dist)
  return ans

def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    tok = stdin.readline().split()
    print(solve(int(tok[0]), int(tok[1])))
    tcnt -= 1

main()