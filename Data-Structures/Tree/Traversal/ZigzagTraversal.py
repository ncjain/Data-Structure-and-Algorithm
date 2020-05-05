class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None
  
def zizagtraversal(root): 
    if root is None: 
        return
    currentLevel = [] 
    nextLevel = [] 
    ltr = True
    currentLevel.append(root) 
    while len(currentLevel) > 0: 
        temp = currentLevel.pop(-1) 
        print(temp.data, " ", end="") 
        if ltr: 
            if temp.left: 
                nextLevel.append(temp.left) 
            if temp.right: 
                nextLevel.append(temp.right) 
        else: 
            if temp.right: 
                nextLevel.append(temp.right) 
            if temp.left: 
                nextLevel.append(temp.left) 
  
        if len(currentLevel) == 0: 
            ltr = not ltr 
            currentLevel, nextLevel = nextLevel, currentLevel 


def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1):
        if i%2 == 0:
            printGivenLevel(root, i,False)
        else:
            printGivenLevel(root, i,True)

def printGivenLevel(root , level, ltr): 
    if root is None: 
        return
    if level == 1: 
        print(root.data, " ", end="") 
    elif level > 1 :
        if ltr:
            printGivenLevel(root.left , level-1, ltr) 
            printGivenLevel(root.right , level-1, ltr)
        else:
            printGivenLevel(root.right , level-1, ltr)
            printGivenLevel(root.left , level-1, ltr) 

def height(node): 
    if node is None: 
        return 0 
    else : 
        lheight = height(node.left) 
        rheight = height(node.right) 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

if __name__ == "__main__":
	root = Node(1) 
	root.left = Node(3) 
	root.right = Node(2) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
	root.right.left = Node(6) 
	root.right.right = Node(7)
	print("Zigzag Order traversal of binary tree is") 
	printLevelOrder(root)
	print("\nZigzag Order traversal of binary tree is") 
	zizagtraversal(root)
	print("\nZigzag Order traversal of binary tree is") 
	iterativeLevelorder(root) 