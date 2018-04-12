###Lab 4: Binary search trees
In this assignment, you will use the provided template code to implement a binary search tree that can store keys and their associated data (much like a dictionary). The main class is BinarySearchTree and it uses a Node internally to build the search tree.

###A basic solution
Implement the methods 
*size
*find
*insert
*remove
as the first basic interface for the class. A KeyError exception should be raised for remove and find if the given key is not in the search tree. If k is a key already in the tree, then the old value should be replaced with the new value.

##Example usage
  credits = BinarySearchTree()
  credits.insert('DA3018', 7.5)
  credits.insert('DA2004', 7.5)
  credits.insert('DA2003', 6)
  n = credits.size()          # n = 3
  hp = credits.find('DA3018') # set hp to 7.5
  credits.remove('DA2003')
  m = credits.size()          # m = 2

##Requirements
*You must use a binary search tree internally and you are not allowed to make use of a dictionary, list, or other datastructure in Python's libraries.
*You may extend the given interface, but not change the suggested methods.
*Use the proper exception handling, as indicated above!

##Hint
It is strongly suggested to use recursion for all (?) operations. 

##For grading
1.Show your code and demonstrate how it works using a small example program.
2. What is the time complexity of the operations?

###Add an iterator interface
Add an iterator interface to BinarySearchTree, so that you can iterate through key and value pairs using an ordingary for loop:
  for course, hp in credits:
      print(course)
Use a generator to implement the iterator! Generators is an easy way to achieve iterators: you simple write code (for example a loop or a recursion) to iterate through your elements and use the  yield  and  yield from  statements whenever you reach an element to return. To design a generator, you can pretend that you want to print all elements rather than return them; then you substitute all print statements with yield.

You can read more about iterators and generators here and other places on the web (but be careful to note the Python version!).

##Requirement
You must use a genererator.

##For grading
3. Demonstrate a working iterator interface.
4. Explain how you have used yield.

##Add support for dictionary-style lookups
Add methods __getitem__ and __setitem__ to BinarySearchTree. This will enable constructs like:
  credits['DA2001'] = 15
  print(credits['DA3018'])

##Requirement
When implementing __getitem__ and __setitem__, you must use the previously defined public interface. It is not acceptable to work with the internal representation of BinarySearchTree.

##For grading
5. Demonstrate working insertion and retrieval using the [key] interface.
