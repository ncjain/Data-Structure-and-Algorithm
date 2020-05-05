class DeQueue:
    def __init__(self, capacity):
        print("Created a queue with capacity %d"%(capacity))
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [None]*capacity 

    def isFull(self):
        if ((self.rear + 1) % self.capacity == self.front) or ((self.front - 1) % self.capacity == self.rear):
            return True
        return False
 
    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at front")
            return
        return self.queue[self.front]
 
    def getRear(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at rear")
            return
        return self.queue[self.rear]


    def insetFront(self, data):
        if self.isFull():
            print("Queue is full, can not insert element %d into queue"%(data))
            return
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity # 0
            self.rear = (self.rear + 1) % self.capacity
        else:
            self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = data
        print("Inserted %d in front of queue"%(data))

    def insertRear(self, data):
        if self.isFull():
            print("Queue is full, can not insert element %d into queue"%(data))
            return

        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity # 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        print("Inserted %d into rear of queue"%(data))
      
    def deleteRear(self):
        if self.isEmpty():
            print("Queue is empty, can not delete element from queue")
            return

        data = self.queue[self.rear]
        self.queue[self.rear] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity

        print("Deleted %d from rear of queue"%(data))
        return data

    def deleteFront(self):
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

        print("Deleted %d from front of queue"%(data))
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
    queue = DeQueue(5)
    queue.insetFront(3)
    queue.insetFront(2)
    queue.insetFront(1)
    queue.insertRear(4)
    queue.insertRear(5)
    queue.insetFront(6)
    queue.display()
    queue.deleteRear()
    queue.deleteRear()
    queue.deleteRear()
    queue.deleteRear()
    queue.deleteRear()
    queue.display()
