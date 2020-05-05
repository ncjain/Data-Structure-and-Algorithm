class Node(): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def search(self,key):
        return self._search(self.root,key)

    def _search(self,root,key):
        if root is None or root.val == key: 
            return root 
        if root.val < key: 
            return self._search(root.right,key) 
        return self._search(root.left,key)
    
    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, current, node):
        if current.data < node.data: 
            if current.right is None: 
                current.right = node 
            else: 
                self._insert(current.right, node) 
        else: 
            if current.left is None: 
                current.left = node 
            else: 
                self._insert(current.left, node) 

    def minValueNode(self, node): 
        current = node 
        while(current.left is not None): 
            current = current.left
        return current  

    def delete(self,key):
        return self.deleteNode(self.root, key)

    def deleteNode(self, current, key):
        if current is None: 
            return current
        if key < current.data: 
            current.left = self.deleteNode(current.left, key) 
        elif(key > current.data): 
            current.right = self.deleteNode(current.right, key)
        else:
            # Node with only one child or no child 
            if current.left is None : 
                temp = current.right  
                current = None 
                return temp  
            elif current.right is None : 
                temp = current.left  
                current = None
                return temp
            temp = self.minValueNode(current.right) 
            current.data = temp.data 
            current.right = self.deleteNode(current.right , temp.data) 
        return current


    def inorder(self):
        if not self.root:
            print("There is no element in tree")
            return
        self._inorder(self.root)

    def _inorder(self, temp): 
        if not temp:
            return
        self._inorder(temp.left)
        print(temp.data,end = " ") 
        self._inorder(temp.right)

# Driver code 
if __name__ == '__main__': 
    btree = BinarySearchTree()
    btree.insert(20)
    btree.insert(11)
    btree.insert(9)
    btree.insert(7)
    btree.insert(15)
    btree.insert(8)
    btree.insert(12)
    btree.inorder()
    btree.delete(20)
    btree.inorder()