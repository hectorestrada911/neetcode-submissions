##Need to create 2 stacks one for actually adding/pop values
#The second stack is for tracking the values, without the need
#To iterate all the values, if we iterate through every value and 
#Compare them it would create an O(n) time complexity, instead we can use
#The second stack to keep track, and Keep the O(1) time complexity


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

       

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
        