class QueueNode:
    def __init__(self,data):
        self.data = data
        self.link = None

class QueueList:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return True if self.rear is None and self.front is None else False 
    
    def Front(self):
        if self.isEmpty():
            print("Queue is empty. There is no front element")
            return
        data = self.front.data
        print("Front element in queue is : {}".format(data))
        return data

    def Rear(self):
        if self.isEmpty():
            print("Queue is empty. There is no rear element")
            return
        data = self.rear.data
        print("Rear element in queue is : {}".format(data))
        return data
        
    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        temp = self.front
        while(True):
            print(temp.data)
            if temp == self.rear:
                break
            temp = temp.link
            
    def enqueue(self,data):
        new_node = QueueNode(data)
        if self.isEmpty():
            self.front = new_node
        else:
            self.rear.link = new_node
        self.rear = new_node
        print("Insterd element {} into queue".format(data))
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Can not delete element from queue")
            return
        data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.link
        print("Deleted element {} from queue".format(data))
        return data

        
if __name__ == "__main__":
    queue = QueueList()
    queue.Front()
    queue.Rear()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.Front()
    queue.Rear()
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    queue.Front()
    queue.Rear()
    """
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
    """