# Python program to insert element in binary tree 
"""
Min and Max heap (complete binary tree)
B tree
B+ Tree
Red black tree
Threaded Binary Tree
Skewed Binary Tree
Extended Binary Tree



geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/

https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
https://www.geeksforgeeks.org/avl-with-duplicate-keys/
https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/

Graph:
https://www.geeksforgeeks.org/applications-of-minimum-spanning-tree/

Why Trees?
1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer:
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays).
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists).
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.

Main applications of trees include:
1. Manipulate hierarchical data.
2. Make information easy to search (see tree traversal).
3. Manipulate sorted lists of data.
4. As a workflow for compositing digital images for visual effects.
5. Router algorithms
6. Form of a multi-stage decision-making (see business chess).

1. Store hierarchical data, like folder structure, organization structure, XML/HTML data.
2. Binary Search Tree is a tree that allows fast search, insert, delete on a sorted data. It also allows finding closest item
3. Heap is a tree data structure which is implemented using arrays and used to implement priority queues.
4. B-Tree and B+ Tree : They are used to implement indexing in databases.
5. Syntax Tree: Used in Compilers.
6. K-D Tree: A space partitioning tree used to organize points in K dimensional space.
7. Trie : Used to implement dictionaries with prefix lookup.
8. Suffix Tree : For quick pattern searching in a fixed text.
9. Spanning Trees and shortest path trees are used in routers and bridges respectively in computer networks

Balanced Binary Tree
A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. For Example, AVL tree maintains O(Log n) height by making sure that the difference between heights of left and right subtrees is atmost 1. Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
"""
class Node(): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self,data):
        temp = self.root
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            q = [] 
            q.append(temp) 

            # Do level order traversal until we find an empty place. 
            while (len(q)): 
                temp = q[0] 
                q.pop(0) 

                if (not temp.left): 
                    temp.left =  new_node
                    break
                else: 
                    q.append(temp.left) 

                if (not temp.right): 
                    temp.right = new_node 
                    break
                else: 
                    q.append(temp.right) 

    def deleteDeepest(self, d_node): 
        q = [] 
        q.append(self.root) 
        while(len(q)): 
            temp = q.pop(0) 
            if temp is d_node: 
                temp = None
                return
            if temp.right: 
                if temp.right is d_node: 
                    temp.right = None
                    return
                else: 
                    q.append(temp.right) 
            if temp.left: 
                if temp.left is d_node: 
                    temp.left = None
                    return
                else: 
                    q.append(temp.left) 
       
    # function to delete element in binary tree  
    def deletion(self, key): 
        if self.root == None : 
            return None
        if self.root.left == None and self.root.right == None: 
            if self.root.key == key :  
                return None
            else : 
                return self.root 
        key_node = None
        q = [] 
        q.append(self.root) 
        while(len(q)): 
            temp = q.pop(0) 
            if temp.data == key: 
                key_node = temp 
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
        if key_node :  
            x = temp.data 
            self.deleteDeepest(temp) 
            key_node.data = x 
        return self.root

    def size(self):
        return self._size(self.root)
        
    def _size(self, node): 
        if node is None: 
            return 0 
        else: 
            return (self._size(node.left)+ 1 + self._size(node.right))

    def findMax(self):
        return self._findMax(self.root)
        
    def _findMax(self, root):
        if (root == None):  
            return -1
 
        res = root.data 
        lres = self._findMax(root.left)  
        rres = self._findMax(root.right)  
        if (lres > res): 
            res = lres  
        if (rres > res):  
            res = rres  
        return res


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
    
    def iterativeInorder(self):
        current = self.root  
        stack = []          
        while True: 
            if current is not None: 
                stack.append(current) 
                current = current.left  
            elif(stack): 
                current = stack.pop() 
                print(current.data, end=" ")
                current = current.right  
            else: 
                break

    # Inorder traversal without recursion and without stack
    def MorrisInorderTraversal(self):
        current = self.root
        while(current is not None):
            if current.left is None:
                print(current.data, end= " ")
                current = current.right
            else:
                pre = current.left
                while(pre.right is not None and pre.right != current):
                    pre = pre.right

                if(pre.right is None):
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    print(current.data, end= " ")
                    current = current.right

    def preorder(self):
        if not self.root:
            print("There is no element in tree")
            return
        self._preorder(self.root)

    def _preorder(self, temp): 
        if not temp:
            return
        print(temp.data,end = " ")
        self._preorder(temp.left)
        self._preorder(temp.right)
        
    def iterativePreorder(self): 
        if self.root is None: 
            return 
        stack = [] 
        stack.append(self.root) 
        while stack: 
            node = stack.pop() 
            print(node.data, end=" ")
            if node.right is not None: 
                stack.append(node.right) 
            if node.left is not None: 
                stack.append(node.left)

    # Preorder traversal without recursion and without stack
    def MorrisPreorderTraversal(self):
        curr = self.root
        while curr:
            if curr.left is None:
                print(curr.data, end= " ")
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right is not curr:
                    prev = prev.right

                if prev.right is curr:
                    prev.right = None
                    curr = curr.right
                else:
                    print(curr.data, end=" ")
                    prev.right = curr
                    curr = curr.left
                
    def postorder(self):
        if not self.root:
            print("There is no element in tree")
            return
        self._postorder(self.root)

    def _postorder(self, temp): 
        if not temp:
            return
        self._postorder(temp.left)
        self._postorder(temp.right)
        print(temp.data,end = " ")

    def iterativePostorder(self): 
        if self.root is None: 
            return 
        stack1 = []
        stack2 = []
        stack1.append(self.root) 
        while stack1: 
            node = stack1.pop() 
            stack2.append(node) 
            if node.left is not None: 
                stack1.append(node.left)
            if node.right is not None: 
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().data, end=" ")
    
    # Postorder traversal without recursion and without stack    
    def postorderDFS(self): 
        """In this method a DFS based solution is discussed. We keep track of visited nodes in a hash table."""
        temp = self.root  
        visited = set() 
        while (temp and temp not in visited): 
            # Visited left subtree  
            if (temp.left and temp.left not in visited): 
                temp = temp.left  
                  
            # Visited right subtree  
            elif (temp.right and temp.right not in visited): 
                temp = temp.right  
              
            # Print node  
            else: 
                print(temp.data, end = " ")  
                visited.add(temp)  
                temp = self.root

    def iterativeLevelorder(self):
        if not self.root:
            print("There is no element in tree")
            return    
        q = [] 
        q.append(self.root) 
        while(len(q)): 
            temp = q.pop(0) 
            print("%d"%(temp.data),end = " ") 
            if temp.left: 
                q.append(temp.left)
            if temp.right:  
                q.append(temp.right)
                
"""
Inorder Tree Traversal with Recursion
Inorder Tree Traversal without Recursion
Inorder Tree Traversal without recursion and without stack!
nth-node from inorder-traversal
"""
# Driver code 
if __name__ == '__main__': 
    btree = BinaryTree()
    btree.insert(20)
    btree.insert(11)
    btree.insert(9)
    btree.insert(7)
    btree.insert(15)
    btree.insert(8)
    btree.insert(12)
    print("Inorder traversal without recursion:", end = " ") 
    btree.iterativeInorder()
    print()
    print("Inorder traversal with recursion:", end = " ") 
    btree.inorder()
    print()
    print("Inorder traversal without recursion and without stack:", end = " ") 
    btree.MorrisInorderTraversal()
    print()
    print("Preorder traversal without recursion:", end = " ") 
    btree.iterativePreorder()
    print()
    print("Preorder traversal with recursion:", end = " ") 
    btree.preorder()
    print()
    print("Preorder traversal without recursion and without stack:", end = " ") 
    btree.MorrisPreorderTraversal()
    print()
    print("Postorder traversal without recursion:", end = " ") 
    btree.iterativePostorder()
    print()
    print("Postorder traversal with recursion:", end = " ") 
    btree.postorder()
    print()
    print("Postorder traversal without recursion and without stack:", end = " ") 
    btree.postorderDFS()