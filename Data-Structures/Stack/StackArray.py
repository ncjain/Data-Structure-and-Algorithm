class StackArray:
    def __init__(self, capacity):
        print("Created stack with capacity {}".format(capacity))
        self.capacity = capacity
        self.top = -1
        self.stack = [None]*capacity 

    def isFull(self):
        if self.capacity - 1 == self.top:
            return True
        return False
        
    def isEmpty(self):
        return True if self.top == -1 else False 
        
    def peek(self):
        if (self.isEmpty()):
            print("Stack is empty. There is no top element")
            return
        data = self.stack[self.top]
        print("Top element {} in stack".format(data))
        return data
    
    def display(self):
        i = self.top
        while( i>=0 ):
            print(self.stack[i])
            i = i - 1
            
    def push(self, data):
        if (self.isFull()):
            print("Stack is full, can not push element")
            return
        self.top = self.top + 1
        self.stack[self.top] = data
        print("Pushed element {} into stack".format(data))
        
    def pop(self):
        if (self.isEmpty()):
            print("Stack is empty, can not pop element")
            return
        item = self.stack[self.top]
        self.top = self.top - 1
        print("Poped element {} from stack".format(item))
        return item
        
        
if __name__ == "__main__":
    stack = StackArray(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.display()
    stack.peek()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.display()
    stack.peek()
    """
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
    """