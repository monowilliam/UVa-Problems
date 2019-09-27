#William Aguirre Zapata mice.py
from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def sssp(G,source):
	dist = [ INF for i in range(len(G)) ] ; dist[source] = 0
	visited = [ False for i in range(len(G)) ]
	heap = [ (0,source) ]
	while len(heap)!=0:
		d,u = heappop(heap)
		if not(visited[u]):
			visited[u] = True
			for v,w in G[u]:
				if dist[v]>d+w:
					dist[v] = d+w
				heappush(heap,(dist[v],v))
	return dist

def solve(E,T,grafo):
	nratones,ans = sssp(grafo,E-1),0
	for i in nratones:
		if i <= T: ans += 1
	return ans

def main():
	cont = int(stdin.readline())
	while cont:
		stdin.readline()
		N,E,T,M = int(stdin.readline()), int(stdin.readline()), int(stdin.readline()), int(stdin.readline())
		grafo = [[] for _ in range(N)]
		for i in range(M):
			a,b,d = map(int, stdin.readline().split())
			grafo[b-1].append((a-1, d))
		print(solve(E,T,grafo))
		cont-=1
		if cont!=0: print("")

main()