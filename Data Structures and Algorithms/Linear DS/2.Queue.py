#!/usr/bin/python3


class Queue:
    ''' First in First out/Served Data Structure. Item is inserted at front end only and removed from the rear end only'''

    def __init__(self):
        # let's use list as base of implementation
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # insert(0, item) : appends item to index 0 i.e at first index always and shiftss other items to the next index
        # i.e inserting new item at the begining of the list
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return ' '.join(map(str, self.items))


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(20)
    print(q.dequeue())
