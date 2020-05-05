class DeQueueNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DeQueueDLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return True if self.rear is None and self.front is None else False 
    
    def getFront(self):
        if self.isEmpty():
            print("Queue is empty. There is no front element")
            return
        data = self.front.data
        print("Front element in queue is : {}".format(data))
        return data

    def getRear(self):
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
            temp = temp.next
            
    def insertFront(self,data):
        new_node = DeQueueNode(data)
        if self.isEmpty():
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
        self.front = new_node
        print("Inserted element {} in front of queue".format(data))

    def insertRear(self,data):
        new_node = DeQueueNode(data)
        if self.isEmpty():
            self.front = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node 
        self.rear = new_node
        print("Inserted element {} in rear of queue".format(data))
        
    def deleteFront(self):
        if self.isEmpty():
            print("Queue is empty. Can not delete element from queue")
            return
        data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        print("Deleted element {} from front of queue".format(data))
        return data
        
    def deleteRear(self):
        if self.isEmpty():
            print("Queue is empty. Can not delete element from queue")
            return
        data = self.rear.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        print("Deleted element {} from rear of queue".format(data))
        return data

        
if __name__ == "__main__":
    queue = DeQueueDLL()
    queue.insertRear(10)
    queue.insertRear(15)
    queue.insertRear(20)
    queue.insertFront(5)
    queue.insertFront(0)
    queue.getFront()
    queue.getRear()
    queue.display()
    queue.deleteFront()
    queue.getFront()
    queue.getRear()
    queue.display()
    queue.deleteRear()
    queue.getFront()
    queue.getRear()
    queue.display()