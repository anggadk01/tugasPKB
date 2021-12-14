# Python program IDS
from collections import defaultdict

# Daftar representation
class Graph:

	def __init__(self,vertices):

		
		self.V = vertices

		# dictionary graph
		self.graph = defaultdict(list)

	
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function to perform a Depth-Limited search
	# dimulai source
	def DLS(self,src,target,maxDepth):

		if src == target : return True

		# kedalaman interasi
		if maxDepth < 0 : return False

	
		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False


	def IDDFS(self,src, target, maxDepth):

	
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False

# buat grafik ids
g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
  
target = 0; maxDepth = 0; src = 0

if g.IDDFS(src, target, maxDepth) == True:
	print ("Selamat!!! \n" +
		"Input target anda dapat dijangkau dengan kedalaman maksimal :)")
else :
	print ("Huffttt maaf ya :( \n" +
		"Input target anda tidak dapat dijangkau dengan kedalaman maksimal.")

