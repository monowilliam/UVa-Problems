#William Aguirre Zapata sequence.py
from sys import stdin

MAX = 31270

def busquedaBinaria(a,x):
  low = 0
  hi = len(a)-1
  while low <= hi:
    mid = low + ((hi-low)>>1)
    if a[mid] <= x:
      low = mid+1
    else:
      hi = mid-1
  return low

def dig_up_to(n):
  ans = None
  if n<10: ans = n
  elif n<100: ans = 9+((n-9)<<1)
  elif n<1000: ans = 189 + ((n-99)*3)
  elif n<10000: ans = 2889 + ((n-999)*4)
  elif n<100000: ans = 38889 + ((n-9999)*5)
  else: ans = 0
  return ans

def solve(n,arr2,Sk):
  ans = None
  n-=1
  k = arr2[busquedaBinaria(arr2,n)-1]
  ans=Sk[n-k]
  return ans

def main():
  arr1, arr2, i = [], [0], 1
  while i < MAX:
    arr1.append(str(i))
    i+=1
  Sk = "".join(arr1)
  i=1
  while i<MAX:
    temp = dig_up_to(i)
    arr2.append(temp+arr2[i-1])
    i+=1
  tcnt = int(stdin.readline())
  while tcnt!=0:
    print(solve(int(stdin.readline()),arr2,Sk))
    tcnt -= 1

main()