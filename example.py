from egg.resources.structures import Stack

pilita = Stack([1,2])

i = pilita.Iterator()

for index in i.indexes:
    print(i.value)
    i.next()

print(type(i))