#William Aguirre Zapata airports.py
from sys import stdin

class dforest(object):
	"""implement an union-find"""

	def __init__(self, size=100):
		"""create an empty disjoint forest"""
		self.__parent = [ i for i in range(size) ]
		self.__rank = [ 0 for _ in range(size) ]
		self.__ccount = self.__size = size

	def __str__(self):
		"""return the string representation"""
		return str(self.__parent)

	def find(self, x):
		"""return the representative of x"""
		if self.__parent[x]!=x: self.__parent[x] = self.find(self.__parent[x])
		return self.__parent[x]

	def ccount(self):
		"""return the number of components"""
		return self.__ccount

	def union(self, x, y):
		"""perform the union of the collections where x and y belong"""
		rx,ry = self.find(x),self.find(y)
		if rx != ry:
			krx,kry = self.__rank[rx],self.__rank[ry]
			if krx > kry:
				self.__parent[ry] = rx
			else:
				self.__parent[rx] = ry
				if krx == kry:
					self.__rank[ry] += 1
			self.__ccount -= 1

def kruskal(grafo,N):
	grafo.sort(key = lambda x: x[2])
	df,i,ans,c = dforest(N),0,0,-1
	while i != len(grafo) and A>c:
		u,v,c = grafo[i]
		if df.find(u) != df.find(v) and A>c:
			df.union(u,v)
			ans+=c
		i+=1
	i=df.ccount()
	ans += i*A
	return ans,i

def main():
	global A
	T,X1 = int(stdin.readline()),1
	while T:
		N,M,A = map(int, stdin.readline().split())
		grafo = []
		for i in range(M):
			X,Y,C = map(int, stdin.readline().split())
			grafo.append((X-1, Y-1, C))
		Y1,Z = kruskal(grafo, N)
		print('Case #{0}: {1} {2}'.format(X1, Y1, Z))
		X1+=1
		T-=1
	
main()