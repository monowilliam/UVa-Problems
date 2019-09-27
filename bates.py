#William Aguirre Zapata bates.py
from sys import stdin

INF = float('inf')

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

def solve(text, p, dicc):
  ans,first,last = None,None,None
  i,band = 0,0
  n = -INF
  while i < len(p) and len(text) > 0 and not band:
    if p[i] in dicc.keys():
      ans = busquedaBinaria(dicc[p[i]],n)
      if ans >= len(dicc[p[i]]):
        band = 1 
      else:
        band
      if not band:
        if i == 0:
          first = dicc[p[i]][ans]
        n = dicc[p[i]][ans]
        i+=1
    else:
      band = 1
  if len(text)>0 and not band:
    last = dicc[p[i-1]][ans]
  else:
    ans = None
  return ans,first,last

def main():
  text = stdin.readline().strip()
  tcnt = int(stdin.readline())
  dicc = {}
  i = 0
  for k in text:
    if k not in dicc.keys():
      dicc[k]=[i]
    else:
      dicc[k].append(i)
    i+=1
  while tcnt!=0:
    p = stdin.readline().strip()
    ans,first,last = solve(text, p, dicc)
    if ans: print('Matched {0} {1}'.format(first, last))
    else: print('Not matched')
    tcnt -= 1

main()