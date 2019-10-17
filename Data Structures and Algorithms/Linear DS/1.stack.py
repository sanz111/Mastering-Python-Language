#!/usr/bin/python3


class Stack:
    '''Last in First Out Data Structure. Item is inserted and removed from only one end called top'''

    def __init__(self):
        # using list as base of the Stack Implementation
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        # inserting item at the next index
        self.items.append(item)
        # self.items.insert(len(self.items), item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack is Empty"
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return "Stack is Empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return ' '.join(map(str, self.items))


if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(49)
    s.push(55)
    s.push(12)
    s.push(10)
    s.push(5)
    print(s)
    s.pop()
    print(s)
