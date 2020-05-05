"""
Priority Queue Applications
Some of the applications of a priority queue are:

Dijkstra's algorithm
for implementing stack
for load balancing and interrupt handling in an operating system
for data compression in Huffman code
"""

class QueueNode:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        self.next = None

class ProrityQueueSLL:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False 
    
    def top(self):
        if self.isEmpty():
            print("Queue is empty. There is no rear element")
            return
        data = self.head.data
        print("Rear element in queue is : {}".format(data))
        return data
        
    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def push(self,data,priority):
        new_node = QueueNode(data, priority)
        if self.isEmpty():
            self.head = new_node
        else:
            if self.head.priority > priority:
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                while(temp.next != None and temp.next.priority <= priority):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
        print("Insterd element {} into queue".format(data))
    
    def pop(self):
        if self.isEmpty():
            print("Queue is empty. Can not delete element from queue")
            return
        data = self.head.data
        self.head = self.head.next
        print("Deleted element {} from queue".format(data))
        return data

        
if __name__ == "__main__":
    queue = ProrityQueueSLL()
    queue.top()
    queue.push(1,1)
    queue.push(3,3)
    queue.push(5,5)
    queue.push(4,4)
    queue.push(2,2)
    queue.push(10,5)
    queue.display()
    queue.pop()
    queue.top()
    queue.display()
    """
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
    """