class CircularQueueArray:
    def __init__(self, capacity):
        print("Created a queue with capacity %d"%(capacity))
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [None]*capacity 


    def isFull(self):
        if (self.rear + 1) % self.capacity == self.front:
            return True
        return False

    
    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    
    def Front(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at front")
            return
        return self.queue[self.front]

        
    def Rear(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at rear")
            return
        return self.queue[self.rear]

        
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full, can not insert element %d into queue"%(data))
            return

        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity # 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        print("Inserted %d into queue"%(data))

      
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, can not delete element from queue")
            return

        data = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print("Deleted %d from queue"%(data))
        return data


    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        i = self.front
        print("Element in queue are")
        while( True ):
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity


if __name__ == "__main__":
    queue = CircularQueueArray(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
    queue.enqueue(6)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(6)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    queue.enqueue(11)
    queue.display()