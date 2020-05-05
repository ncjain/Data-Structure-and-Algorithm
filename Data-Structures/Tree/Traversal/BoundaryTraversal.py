"""
We break the problem in 3 parts:
1. Print the left boundary in top-down manner.
2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts:
…..2.1 Print all leaf nodes of left sub-tree from left to right.
…..2.2 Print all leaf nodes of right subtree from left to right.
3. Print the right boundary in bottom-up manner.
"""
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def printLeaves(root): 
    if(root): 
        printLeaves(root.left) 
        if root.left is None and root.right is None: 
            print(root.data), 
        printLeaves(root.right) 
  
def printBoundaryLeft(root): 
    if(root): 
        if (root.left): 
            print(root.data) 
            printBoundaryLeft(root.left) 
          
        elif(root.right): 
            print (root.data) 
            printBoundaryLeft(root.right) 

def printBoundaryRight(root): 
    if(root): 
        if (root.right): 
            printBoundaryRight(root.right) 
            print(root.data) 
          
        elif(root.left): 
            printBoundaryRight(root.left) 
            print(root.data)

def printBoundary(root): 
    if (root): 
        print(root.data) 
        printBoundaryLeft(root.left) 
        printLeaves(root.left) 
        printLeaves(root.right) 
        printBoundaryRight(root.right) 
  
  


root = Node(1)

root.left = Node(2)
root.right = Node(13)

root.left.left = Node(3)
root.left.right = Node(14)
root.right.left = Node(15)
root.right.right = Node(12)

root.left.left.left = Node(4)
root.left.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

printBoundary(root) 