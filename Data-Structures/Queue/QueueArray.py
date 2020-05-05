class QueueArray:
    def __init__(self, capacity):
        print("Created a queue with capacity %d"%(capacity))
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [None]*capacity 


    def isFull(self):
        if self.rear == self.capacity - 1:
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
            self.front += 1

        self.rear += 1
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
            self.front += 1

        print("Deleted %d from queue"%(data))
        return data


    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        i = self.front
        print("Element in queue are")
        while( i <= self.rear):
            print(self.queue[i])
            i += 1


if __name__ == "__main__":
    queue = QueueArray(5)
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
    queue.dequeue()
    queue.enqueue(6)
    queue.dequeue()
    queue.dequeue()
    queue.display()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()