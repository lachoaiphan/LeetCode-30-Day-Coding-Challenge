"""
Prompt:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

# My implementation of minStack. For the minimum value, it is reliant on the element's index


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_index = -1
        self.length = 0

    def push(self, x: int):
        if self.min_index >= 0:
            if x < self.stack[self.min_index]:
                self.min_index = self.length
        else:
            self.min_index = 0
        self.stack.append(x)
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Stack is empty!")
        if self.min_index == self.length - 1:
            if self.length == 1:
                self.min_index = -1
            else:
                self.min_index = 0
                for index in range(0, self.length - 1):
                    if self.stack[self.min_index] > self.stack[index]:
                        self.min_index = index
        del self.stack[self.length - 1]
        self.length -= 1

    def top(self):
        if self.length == 0:
            raise Exception("Stack is empty!")
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        if self.length == 0:
            raise Exception("Stack is empty!")
        return self.stack[self.min_index]


# Test Case
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output -3

min_stack.pop()
print(min_stack.top())  # Output 0
print(min_stack.getMin())  # Output -2
