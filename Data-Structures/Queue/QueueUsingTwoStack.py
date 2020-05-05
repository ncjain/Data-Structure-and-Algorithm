class QueueEnqueueCostly:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top1 = -1
        self.top2 = -1
        self.stack1 = [None]*capacity
        self.stack2 = [None]*capacity

    def push1(self,data):
        self.top1 += 1
        self.stack1[self.top1] = data

    def push2(self,data):
        self.top2 += 1
        self.stack2[self.top2] = data   

    def pop1(self):
        data = self.stack1[self.top1]
        self.stack1[self.top1] = None
        self.top1 -= 1
        return data

    def pop2(self):
        data = self.stack2[self.top2]
        self.stack2[self.top2] = None
        self.top2 -= 1
        return data
        
    def isFull(self):
        if self.top1 == self.capacity -1:
            return True
        return False

    def isEmpty(self):
        if self.top1 == -1:
            return True
        return False

    def Front(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at front")
            return
        data = self.stack1[self.top1]
        print("Front element in queue is : %d"%(data))
        return data
        
    def Rear(self):
        if self.isEmpty():
            print("Queue is empty, there is no element at rear")
            return
        data = self.stack1[0]
        print("Rear element in queue is : %d"%(data))
        return data
        
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full, can not insert element")
            return
        while(self.top1 != -1):
            self.push2(self.pop1())
        
        self.push1(data)

        while(self.top2 != -1):
            self.push1(self.pop2())
        
        print("Inserted element %d into queue"%(data))
   
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, can not delete element")
            return
        data = self.pop1()
        print("Deleted element %d from queue"%(data))
        return data
        
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        i = self.top1
        while(i>=0):
            print(self.stack1[i])
            i -= 1


class QueueDequeueCostly:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top1 = -1
        self.top2 = -1
        self.stack1 = [None]*capacity
        self.stack2 = [None]*capacity

    def push1(self,data):
        self.top1 += 1
        self.stack1[self.top1] = data

    def push2(self,data):
        self.top2 += 1
        self.stack2[self.top2] = data   

    def pop1(self):
        data = self.stack1[self.top1]
        self.stack1[self.top1] = None
        self.top1 -= 1
        return data

    def pop2(self):
        data = self.stack2[self.top2]
        self.stack2[self.top2] = None
        self.top2 -= 1
        return data
        
    def isFull(self):
        if self.top1 + self.top2 + 2 == self.capacity:
            return True
        return False

    def isEmpty(self):
        if self.top1 == -1:
            return True
        return False

    def Front(self):
        if self.isEmpty() and self.top2 == -1:
            print("Queue is empty, there is no element at front")
            return
        data = self.stack2[self.top2] or self.stack1[0]
        print("Front element in queue is : %d"%(data))
        return data
        
    def Rear(self):
        if self.isEmpty() and self.top2 == -1:
            print("Queue is empty, there is no element at rear")
            return
        data = self.stack1[self.top1] or self.stack2[0]
        print("Rear element in queue is : %d"%(data))
        return data
        
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full, can not insert element")
            return
        self.push1(data)
        print("Inserted element %d into queue"%(data))
   
    def dequeue(self):
        if self.isEmpty() and self.top2 == -1:
            print("Queue is empty, can not delete element")
            return
            
        if self.top2 == -1:
            while(self.top1 != -1):
                self.push2(self.pop1())
        
        data = self.pop2()
        print("Deleted element %d from queue"%(data))
        return data
    
    def display(self):
        if self.isEmpty() and self.top2 == -1:
            print("Queue is empty")
            return
        i = self.top2
        while(i >= 0):
            print(self.stack2[i])
            i -= 1
        i = 0
        while(i <= self.top1):
            print(self.stack1[i])
            i += 1
            
        
if __name__ == "__main__":
    queue = QueueDequeueCostly(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
    queue.dequeue()
    queue.enqueue(6)
    queue.enqueue(7)
    queue.display()