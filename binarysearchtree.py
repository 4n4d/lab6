# Lab 5
class Node:
    def __init__(self, key, val):
        self._key = key
        self._val = val
        self._left = None
        self._right = None

    def set_children(self, l, r):
        self._left = l
        self._right = r

    def data(self):
        return self._key, self._val

    def left_child(self):
        return self._left

    def right_child(self):
        return self._right

    def set_value(self, val):
        self._val = val

    def set_key(self, key):
        self._key = key
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        '''
        Public interface method to insert a key and value to the search tree.
        '''

        # modified this function a bit, self.root should always be the root?
        if self.root == None:
            self.root = self.__insert(self.root, key, val)
        else:
            self.__insert(self.root, key, val)
            
    def __insert(self, v, key, val):
        '''
        Internal method to recursively decide where to insert a new node.
        Warning! This method has a bug, it does not behave according to specification!
        '''
        # if the key is equal we want to update the value at the key
        
        if v:
            v_key, x = v.data() # Ignoring x actually
            left = v.left_child()
            right = v.right_child()
            if key < v_key:
                left = self.__insert(left, key, val)
            elif key > v_key:
                right = self.__insert(right, key, val)
            else:
                v.set_value(val)
            v.set_children(left, right)
            return v
        else:
            return Node(key, val)

    def find(self, key):
        v = self.__find(self.root, key)
        if v == None:
            return None
        return v

    def __find(self, v, key):
        if v:
            v_key, x = v.data()
            if v_key == key:
                return x
            elif v_key < key:
                return self.__find(v.left_child(), key)
            else:
                return self.__find(v.right_child(), key)
        else:
            return None

    def remove(self, key):
        if self.__remove(self.root, None, key, 0) == 0:
            raise KeyError
        
    def __remove(self, v, parent, key, i):
        if v or i>0:
            v_key, x = v.data()
            if key == v_key:
                #found, start removal procedure...
                # if both nodes are empty, we can just remove it
                if v.left_child() == None and v.right_child() == None:
                    if parent.left_child().data()[0]==key:
                        parent.set_children(None, parent.right_child())
                    else:
                        parent.set_children(parent.left_child(), None)

                # if one of the nodes are empty, we can just set this node to the next node
                elif v.left_child() == None:
                    if parent.left_child().data()[0]==key:
                        parent.set_children(v.right_child(), parent.right_child())
                    else:
                        parent.set_children(parent.left_child(), v.right_child())

                elif v.right_child() == None:
                    if parent.left_child().data()[0]==key:
                        parent.set_children(v.left_child(), parent.right_child())
                    else:
                        parent.set_children(parent.left_child(), v.left_child())
                # if none of the nodes are empty then we have to think... differently
                else:
                    # in this case we want to go to the right node (which we know is empty)
                    # we go as far to the left as we can
                    # when we cant go left anymore we have found the minimum value in the right tree. We set v to the minimum value
                    # then we take the parent of the minimum value and repoint it to the right element of the minimum value.

                    minNode = v.right_child()
                    minParent = None

                    if not (minNode.left_child() == None):
                        while not (minNode.left_child() == None):
                            minParent = minNode
                            minNode = minNode.left_child()

                        if parent.left_child().data()[0]==key:
                            parent.left_child().set_value(minNode.data()[1])
                            parent.left_child().set_key(minNode.data()[0])
                        else:
                            parent.right_child().set_value(minNode.data()[1])
                            parent.right_child().set_key(minNode.data()[0])
                        
                        minParent.set_children(minNode.right_child(), minParent.right_child())
                    else:
                        # if the first element is the minimum value
                        if parent.left_child().data()[0]==key:
                            parent.left_child().set_value(minNode.data()[1])
                            parent.left_child().set_key(minNode.data()[0])
                            parent.left_child().set_children(v.left_child(), minNode.right_child())
                        else:
                            parent.right_child().set_value(minNode.data()[1])
                            parent.right_child().set_key(minNode.data()[0])
                            parent.right_child().set_children(v.left_child(), minNode.right_child())
                return 1+i
            # search children nodes
            return i + self.__remove(v.left_child(), v, key, i) + self.__remove(v.right_child(), v, key, i)
        else:
            return i
        pass
        
    def size(self):
        return self.__size(self.root)

    def __size(self, v):
        if v:
            return 1 + self.__size(v.left_child()) + self.__size(v.right_child())
        else:
            return 0
    
    def __str__(self):
        return str(self.root)

def main():
    credits = BinarySearchTree()
    credits.insert('DA3018', 7.5)
    credits.insert('DA2004', 7.5)
    credits.insert('DA2003', 6)

    print(credits)
    n = credits.size()          # n = 3
    print n
    hp = credits.find('DA3018') # set hp to 7.5
    print hp
    credits.remove('DA2004')
    m = credits.size()          # m = 2
    print m
    
if __name__ == '__main__':
    main()    
