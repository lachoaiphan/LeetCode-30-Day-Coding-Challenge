"""
Prompt:
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
"""

# Designed this FirstUnique class with a queue and two sets.


class FirstUnique:
    def __init__(self, nums):
        self.queue = []
        self.unique_set = set([])
        self.non_unique_set = set([])
        for index in range(0, len(nums)):
            self.add(nums[index])

    def showFirstUnique(self):
        if len(self.queue) > 0:
            while len(self.queue) > 0:
                if self.queue[0] in self.non_unique_set:
                    self.queue.pop(0)
                else:
                    return self.queue[0]
        return -1

    def add(self, value):
        if value not in self.non_unique_set and value not in self.unique_set:
            self.unique_set.add(value)
        elif value not in self.non_unique_set and value in self.unique_set:
            self.non_unique_set.add(value)
        self.queue.append(value)


obj = FirstUnique([2, 3, 5])
print(obj.showFirstUnique())
obj.add(2)
print(obj.showFirstUnique())
