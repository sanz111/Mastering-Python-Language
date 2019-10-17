#!/usr/bin/python3


class Deque:
    ''' Double ended queue is hybridization of stacks (push ,pop) and queue(enqueue)'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return ' '.join(map(str, self.items))


if __name__ == "__main__":
    d = Deque()
    d.addFront(5)
    d.addFront(6)
    d.addRear(4)
    print(d)
    d.removeRear()
    print(d)
    d.removeFront()
    print(d)
