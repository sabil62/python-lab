class BinarySearchTree:
    #initializing the class
    def __init__(self):
        self.root=None    #initially no root node
        self._size=0

    class _BinaryTreeNode:
        def __init__(self,key,value):
            self.left = None  #initially no nodes
            self.right = None
            self.key = key
            self.value=value
    
    # Add a node to the BST
    def add(self, key, value):
        if self.root is None:
            self.root = self._BinaryTreeNode(key, value)
        else:
            stree =self.root
            while True:
                if(key < stree.key):
                    if(stree.left is not None):
                        stree = stree.left
                    else:
                        stree.left = self._BinaryTreeNode(key,value)
                        break
                else:
                    if(stree.right is not None):
                        stree = stree.right
                    else:
                        stree.right = self._BinaryTreeNode(key,value)
                        break
        self._size +=1
        # nod = self._BinaryTreeNode(key,value)
        # store = None
        # rot = self.root

        # while(rot != None):
        #     store = rot
        #     if(key < rot.key):
        #         rot = rot.left
        #     else:
        #         rot = rot.right
        # if (store == None):         #initially when we have to store value
        #     self.root = nod
        # elif (nod.key < store.key):
        #     store.left = rot
        # else:
        #     store.right = rot
        # self._size += 1
         

    # Return the number of nodes in the BST
    def size(self):
        return self._size

    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].
    def inorder_walk(self):
        found = []
        self._inorder(self.root,found)
        return found

    def _inorder(self, stree, found):
        if(stree is not None):
            self._inorder(stree.left,found)
            found.append(stree.key)
            self._inorder(stree.right,found)
        return found

    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        found = []
        self._postorder_walk(self.root,found)
        return found

    def _postorder_walk(self, stree, found ):
        if(stree):
            self._postorder_walk(stree.left, found)
            self._postorder_walk(stree.right, found)
            found.append(stree.key)

    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        found = []
        self._preorder_walk(self.root, found)
        return found
    
    def _preorder_walk(self,stree,found):
        if(stree):
            found.append(stree.key)
            self._preorder_walk(stree.left, found)
            self._preorder_walk(stree.right, found)

    # Search the BST for the given key. Return False if the key is not found.
    def search(self, key):
        sroot = self.root
        while sroot is not None:
            if (key == sroot.key):  #if direct node then return its value
                return sroot.value
            elif (key < sroot.key):     #if the key is less then root then search left subtree
                sroot = sroot.left
            else:                       #if key is greater then root than search rightsubtree
                sroot = sroot.right
        return False                        #else no value

    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self, key):
        stree = self.root
        previous = self.root

        while stree is not None:
            if stree.key == key:    #when found
                
                if stree.left is None and stree.right is None: #end node or leaf nodes
                    stree = None        #delete node here bst will be bst if we delete leaf nodes(no change in property)
                else:

                    if stree.right is None:    #if no right node only
                        if key < previous.key:
                            previous.left = stree.left
                            stree = None            
                        else:
                            previous.right = stree.left
                            stree = None            
                    
                    else:
                        #we have to make a correct binary tree if we delete a node value from midlle
                        # we can do by two methods either greatest value of left 
                        # or smallest value of right, here we do smallest value of right
                        # because it is relatively easier 
                        temp = stree.right
                        temp_previous = stree

                        while temp.left is not None: #until left node is not finished
                            temp_previous = temp
                            temp = temp.left

                        stree.key = temp.key
                        stree.value = temp.value

                        if(temp.key < temp_previous.key):
                            temp_previous.left = None
                        
                        else:
                            temp_previous.right = None

                        del temp
                self._size -= 1
                return True

            elif key < stree.key:
                previous = stree
                stree =  stree.left

            else:
                previous = stree
                stree = stree.right

        return False


    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def smallest(self):
        stre = self.root

        while(stre.left is not None):
            stre = stre.left
        return(stre.key,stre.value)

    #     found =[]
    #     self._smallest(self.root,found)
    #     return found

    # def _smallest(self,stree, found):
    #     if(stree):
    #         if(stree.left == None):#the smallest element lies in left most 
    #             found.append(stree.key)
    #         self._smallest(stree.left, found) #continue going at left side 

    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def largest(self):
        stree = self.root
        while(stree.right is not None): # until we dont find rightmost 
            stree = stree.right        #keep on going right
        return(stree.key, stree.value)


