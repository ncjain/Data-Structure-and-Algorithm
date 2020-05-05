"""
Linked list operation:

1. Insertion:
    1) At the front of the linked list (Time complexity of push() is O(1) as it does constant amount of work.)
    2) After a given node. (Time complexity of insertAfter() is O(1) as it does constant amount of work.)
    3) At the end of the linked list. (Time complexity of append is O(n) where n is the number of nodes in linked list. Since there is a loop from head to end, the function does O(n) work. This method can also be optimized to work in O(1) by keeping an extra pointer to tail of linked list)
    4) After a given position
    5) After a given key
2. Deletion:
    1) Given a key, delete the first occurrence of this key in linked list.
    2) delete the node at a given position 
    3) delete a Linked List
'append',  'insert', 'extend', 'pop', 'remove', 'clear', 'index', 'count', 'copy',  'reverse', 'sort'
"""

class Node: 
	def __init__(self, data): 
		self.data = data
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None

	def push(self, new_data): 

		# 1 & 2: Allocate the Node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 3. Make next of new Node as head 
		new_node.next = self.head 

		# 4. Move the head to point to new Node 
		self.head = new_node 


	# This function is in LinkedList class. Inserts a 
	# new node after the given prev_node. This method is 
	# defined inside LinkedList class shown above */ 
	def insertAfter(self, prev_node, new_data): 

		# 1. check if the given prev_node exists 
		if prev_node is None: 
			print "The given previous node must inLinkedList."
			return

		# 2. create new node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 4. Make next of new Node as next of prev_node 
		new_node.next = prev_node.next

		# 5. make next of prev_node as new_node 
		prev_node.next = new_node 


	# This function is defined in Linked List class 
	# Appends a new node at the end. This method is 
	# defined inside LinkedList class shown above */ 
	def append(self, new_data): 

		# 1. Create a new node 
		# 2. Put in the data 
		# 3. Set next as None 
		new_node = Node(new_data) 

		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
			self.head = new_node 
			return

		# 5. Else traverse till the last node 
		last = self.head 
		while (last.next): 
			last = last.next

		# 6. Change the next of last node 
		last.next = new_node 


	# Utility function to print the linked list 
	def printList(self): 
		temp = self.head 
		while (temp): 
			print temp.data, 
			temp = temp.next


    def delete(self,data):
        temp = self.head
        if temp == None:
            print("List is empty")
            return
        else:
            if temp.data == data:
                print("{} data delted from the head node".format(temp.data))
                self.head = temp.next
                temp = None
                return
            else:                
                pre_temp = None                
                while(temp != None and temp.data != data):
                    pre_temp = temp
                    temp = temp.next
                if temp == None:
                    print("data is not present in the list")
                    return
                print("{} data delted from the list".format(temp.data))
                pre_temp.next = temp.next
                temp = None

# Code execution starts here 
if __name__=='__main__': 

	# Start with the empty list 
	llist = LinkedList() 

	# Insert 6. So linked list becomes 6->None 
	llist.append(6) 

	# Insert 7 at the beginning. So linked list becomes 7->6->None 
	llist.push(7); 

	# Insert 1 at the beginning. So linked list becomes 1->7->6->None 
	llist.push(1); 

	# Insert 4 at the end. So linked list becomes 1->7->6->4->None 
	llist.append(4) 

	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
	llist.insertAfter(llist.head.next, 8) 

	print 'Created linked list is:', 
	llist.printList() 

            

            