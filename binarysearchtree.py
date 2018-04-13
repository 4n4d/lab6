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

        self.root = self.__insert(self.root, key, val)
            
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
        # returns None if the key was not found
        v = self.__find(self.root, key)
        if v == None:
            return None
        return v

    def __find(self, v, key):
        # recursively search through elements, if the key is found, return the value stored in the node
        if v:
            v_key, x = v.data()
            print v_key
            if v_key == key:
                return x
            elif v_key > key:
                return self.__find(v.left_child(), key)
            else:
                return self.__find(v.right_child(), key)
        else:
            return None

    def remove(self, key):
        # if it is 0, no removal was done
        if self.__remove(self.root, None, key, 0) == 0:
            raise KeyError
        
    def __remove(self, v, parent, key, i):
        # when i > 0, we have removed something, hence no need to continue as
        # there is only one entry of any given key
        if v and i == 0:
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

                # if none of the nodes are empty then we have to think differently
                else:    
                # in this case we want to go to the right node (we know it exists)
                # in order to reach the smallest element in this subtree
                # we go as far to the left as we can (while loop)
                # when the smallest element is found, set v to be this element
                # then we need to re-link the parent of the minimum element
                # and any children of the minimum element (will be in the right tree)

                    minNode = v.right_child()
                    minParent = None

                    if not (minNode.left_child() == None):
                        # if the first element is not the minimum value
                        # we must loop down
                        while not (minNode.left_child() == None):
                            minParent = minNode
                            minNode = minNode.left_child()

                        # the element is found now, we do the remapping

                        # we change values of "v" through the parent of "v"
                        # "v" may be the right or the left element of its parent
                        if parent.left_child().data()[0]==key:
                            parent.left_child().set_value(minNode.data()[1])
                            parent.left_child().set_key(minNode.data()[0])
                        else:
                            parent.right_child().set_value(minNode.data()[1])
                            parent.right_child().set_key(minNode.data()[0])

                        # we relink the parent of the min-element
                        minParent.set_children(minNode.right_child(), minParent.right_child())
                    else:
                        # if the first element is the minimum value

                        # similarily, "v" may be the right or left element of its parent
                        if parent.left_child().data()[0]==key:
                            parent.left_child().set_value(minNode.data()[1])
                            parent.left_child().set_key(minNode.data()[0])
                            parent.left_child().set_children(v.left_child(), minNode.right_child())
                        else:
                            parent.right_child().set_value(minNode.data()[1])
                            parent.right_child().set_key(minNode.data()[0])
                            parent.right_child().set_children(v.left_child(), minNode.right_child())
                return 1+i # we increase this as we have removed an element, then the keyerror will not be raised.
            
            # search children nodes
            return i + self.__remove(v.left_child(), v, key, i) + self.__remove(v.right_child(), v, key, i)
        else:
            return i
        
    def size(self):
        # we call the internal recursive size function
        return self.__size(self.root)

    def __size(self, v):
        # adds 1 for all nodes that are non-empty (an empty node will not have
        # any children)
        if v:
            return 1 + self.__size(v.left_child()) + self.__size(v.right_child())
        else:
            return 0
    
    def __str__(self):
        # have done nothing here
        return str(self.root)

    def __iter__(self):
        # another possible way of implementing is probably to use a stack with
        # nodes visited(?) I could not find a way to pass arguments
        # my solution was to list all elements and then in the next()-function
        # simply yield them one by one
        self._list_of_elements = self.__transverse(self.root)
        return self.next()

    def __transverse(self, T):
        if T == None:
            return None

        l = [T.data()]
        
        t = self.__transverse(T.left_child())
        if not t == None:
            l = l + t
            
        t = self.__transverse(T.right_child())
        if not t == None:
            l = l + t

        return l

    def next(self):
        # just loop through the list that was set up by the iter-function that returned
        # this function as the generator function
        for i in self._list_of_elements:
            yield i

    def __getitem__(self, key):
        # use the find function
        return self.find(key)

    def __setitem__(self, key, val):
        # use the insert function
        # (i.e. creates a new element if ['x'] does not exist)
        self.insert(key, val)
    
def main():
    credits = BinarySearchTree()
    credits.insert('DA3018', 7.5)
    credits.insert('DA2004', 7.5)
    credits.insert('DA2003', 6)
    credits.insert('DA2005', 4)
    credits.insert('DA2002', 5)
    credits.insert('DA4020', 10)
    print(credits)
    n = credits.size()          # n = 3
    print n
    hp = credits.find('DA3018') # set hp to 7.5
    print hp
    credits.remove('DA2004')
    m = credits.size()          # m = 2
    print m

    for course, hp in credits:
        print "Course: " + str(course) + " is " + str(hp) + " credits"

    print credits['DA3018']
    credits['DA3018'] = 2
    print credits['DA3018']
    credits['no'] = 10
    print credits['no']

    for course, hp in credits:
        print "Course: " + str(course) + " is " + str(hp) + " credits"
    
if __name__ == '__main__':
    main()    
