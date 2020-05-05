class QueueSingleStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = [None]*capacity

    def push(self,data):
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

        
    def isFull(self):
        if self.top == self.capacity -1:
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def Front(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at front")
            return
        data = self.stack[0]
        print("Front element in queue is : %d"%(data))
        return data
        
    def Rear(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at rear")
            return
        data = self.stack[self.top]
        print("Rear element in queue is : %d"%(data))
        return data
        
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full, can not insert element")
            return
        self.push(data)
        print("Inserted element %d into queue"%(data))
   
    def dequeue(self):
        data = self._dequeue()
        print("Deleted element %d from queue"%(data))

    def _dequeue(self):
        if self.isEmpty():
            print("Queue is empty, can not delete element")
            return
        elif self.top == 0:
            return self.pop()
        else:
            data = self.pop()
            res = self._dequeue()
            self.push(data)
            return res
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        i = 0
        while(i <= self.top):
            print(self.stack[i])
            i += 1
            
        
if __name__ == "__main__":
    queue = QueueDequeueCostly(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.Front()
    queue.Rear()
    queue.display()
    queue.enqueue(6)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.Front()
    queue.Rear()
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.Front()
    queue.Rear()
    queue.display()
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    queue.enqueue(11)
    queue.Front()
    queue.Rear()
    queue.display()


       
        