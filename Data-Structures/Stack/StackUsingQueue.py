class StackNode:
    def __init__(self,data):
        self.data = data
        self.link = None

class StackList:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return True if self.top is None else False 
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty. There is no top element")
            return
        data = self.top.data
        print("Top element {} in stack".format(data))
        return data
        
    def display(self):
        temp = self.top
        while(temp):
            print(temp.data)
            temp = temp.link
            
    def push(self,data):
        new_node = StackNode(data)
        new_node.link = self.top
        self.top = new_node
        print("Pushed element {} into stack".format(data))
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Can not pop element")
            return
        data = self.top.data
        self.top = self.top.link
        print("Pop element {} from stack".format(data))
        return data

        
if __name__ == "__main__":
    stack = StackList()
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