from egg.resources.structures import *

pilita = Stack(["pizza","piña"])

matriz = Matrix(2*[pilita])
matriz.display()

pq = PriorityQueue([1,3,4,3,3,7,1,2])
pq.pop()
pq.pop()
pq.display()

matriz.iterate(print)
