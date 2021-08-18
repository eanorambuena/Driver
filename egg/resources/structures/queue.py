from egg.resources.structures import Iterator

class List():
    def __init__(self, list = []):
        self.list = list
    def reverse(self):
        self.list = self.list.reverse
    def addFirst(self, item):
        self.reverse()
        self.addLast(item)
        self.reverse()
    def addLast(self, item):
        self.list.append(item)
    @property
    def iterator(self):
        return Iterator(self.list)
    @property
    def first(self):
        return self.list[0]
    @property
    def last(self):
        return self.list[0]
    @property
    def size(self):
        return len(self.list)
    @property
    def isEmpty(self):
        return self.size == 0
    
class Queue():
    def __init__(self, list = []):
        self.list = List(list)
    def reverse(self):
        self.list = self.list.reverse
    def put(self, item):
        self.list.addLast(item)
    def Iterator(self):
        return self.list.iterator
    @property
    def first(self):
        return self.list.first
    @property
    def size(self):
        return self.list.size
    @property
    def isEmpty(self):
        return self.list.isEmpty
        
class Stack():
    def __init__(self, list = []):
        self.list = List(list)
    def reverse(self):
        self.list = self.list.reverse
    def put(self, item):
        self.list.addFirst(item)
    def Iterator(self):
        return self.list.iterator
    @property
    def top(self):
        return self.list.first
    @property
    def size(self):
        return self.list.size
    @property
    def isEmpty(self):
        return self.list.isEmpty