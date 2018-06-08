# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 02:32:25 2018

@author: edwar
"""
class ListNode(object):
    """A linked list node."""
    def __init__(self, val=None, nextnode=None):
        self._val, self._next = val, nextnode
        
    def __del__(self): self = None
    
    @property
    def val(self): return self._val
    @val.setter
    def val(self, val):
        self._val = val

    @property
    def next(self): return self._next
    @next.setter
    def next(self, node):
        if isinstance(node, ListNode): self._next = node
        else: raise TypeError\
        ('next node must be of type ListNode. Found {}'.format(type(node)))\
        
    def __str__(self):
        return str(self._val)
    
    def __lt__(self, other):
        if isinstance(other, ListNode): return self.val < other.val
        if not isinstance(other, type(self.val)):
            raise TypeError\
            ("'<' not supported between instances of '{}' and '{}'".format(type(self.val), type(other)))
        else: return self.val < other
        
    def __len__(self): 
        try:
            return len(self.val)
        except TypeError:
            raise TypeError\
            ("object of type '{}' has no len()".format(type(self.val)))
    
    
class TreeNode(object):
    """A Binary Tree Node. Height is base 0"""
    def __init__(self, val=None):
        self._val, self._height, self._isroot = val, 0, False
        self._rchild = self._lchild = None
        
    @property
    def val(self): return self._val
    @val.setter
    def val(self, node): self._val = node
    
    @property
    def lchild(self): return self._lchild
    @lchild.setter
    def lchild(self, node):
        if isinstance(node, TreeNode) or node is None: self._lchild = node
        else: raise TypeError\
        ('next node must be of type TreeNode. Found{}'.format(type(node)))
    
    @property
    def rchild(self): return self._rchild
    @rchild.setter
    def rchild(self, node):
        if isinstance(node, TreeNode) or node is None: self._rchild = node
        else: raise TypeError\
        ('next node must be of type TreeNode. Found{}'.format(type(node)))
        
    @property
    def children(self): return self.lchild, self.rchild
    
    @property
    def isLeaf(self): return self.children == (None, None)
    
    @property
    def isRoot(self): return self._isroot
    
    @property
    def height(self):
        """Max of the child heights plus 1"""
        if self.lchild is not None and self.rchild is not None:
            self._height = max(self.rchild.height, self.lchild.height) + 1
        elif self.lchild: self._height = self.lchild.height + 1
        elif self.rchild: self._height = self.rchild.height + 1
        else: pass
        return self._height
    @height.setter
    def height(self, val): self._height = val
    
    def __add__(self, other):
        if isinstance(other, type(self._val)): return self.val + other
        elif isinstance(other, TreeNode): return self.val + other.val
        else: return NotImplemented
        
    def __sub__(self, other): return self.val - other
    def __rsub__(self, other): return other - self.val
    def __mul__(self, other): return self.val*other
    #def __div__(self, other): return self.val/other
    #def __rdiv__(self, other): return other/self.val
    __rmul__ = __mul__
    __radd__ = __add__
        
    def __lt__(self, other):
        if isinstance(other, TreeNode): return self.val < other.val
        if not isinstance(other, type(self.val)):raise TypeError\
        ("'<' not supported between instances of '{}' and '{}'".format(type(self.val), type(other)))
        else: return self.val < other
        
    def __gt__(self, other):
        if isinstance(other, TreeNode): return self.val > other.val
        if not isinstance(other, type(self.val)):raise TypeError\
        ("'>' not supported between instances of '{}' and '{}'".format(type(self.val), type(other)))
        else: return self.val > other
        
    def __eq__(self, other):
        #return self.val == other.val
        if isinstance(other, TreeNode): return self.val == other.val
        #if not isinstance(other, type(self.val)):raise TypeError\
        #("'==' not supported between instances of '{}' and '{}'".format(type(self.val), type(other)))
        else: return self.val == other
        
    def __str__(self): return str(self.val)
    def __repr__(self): return str(self)
    
    def __iter__(self):
        """Depth First Iteration"""
        if self.lchild is not None: yield from self.lchild
        if self.val is not None: yield self
        if self.rchild is not None: yield from self.rchild
        
    def __getitem__(self, key):
        if not isinstance(key, int) or not isinstance(key, slice): raise TypeError
        i = 0
        while i < key:
            val = next(self)
            i+=1
        return self[key].val
        
    def __reversed__(self):
        """Reversed Depth First Iteration"""
        if self.rchild is not None: yield from self.rchild
        if self.val is not None: yield self
        if self.lchild is not None: yield from self.lchild
        
    
class LinkedList(object):
    """A Singly-Linked List."""
    def __init__(self, l=[]):
        
        self._head = self._tail = self._curr = None
        self._size = 0
        
        while self._size < len(l):
            if self._size == 0:
                newNode = ListNode(l[self._size])
                self._head = newNode
                self._curr = self._head
            else:
                newNode = self._curr._next
                self._curr = newNode
            try: newNode._next = ListNode(l[self._size+1])
            except IndexError:
                self._tail = newNode
            self._size+=1
        self.reset()
    
    def __str__(self):
        return str(self._curr)
    
    @property
    def __len__(self): return self._size
    
    @property
    def head(self): return self._head
    
    @property
    def tail(self): return self._tail
    
    @property
    def curr(self): return self._curr
    
    def traverse(self, n, reset=False):
        """Traverses n places toward the tail from the active node.
        if reset is True, then traversal will commence from the head."""
        i = 0
        if reset: self.reset()
        try:
            while i < n:
                self.curr = self.curr.next 
                i+=1
            return self.curr.val
        except AttributeError:
            self.reset()    # Not sure if resetting is appropriate
            raise IndexError
        
    def pop(self):
        """Retrieves the last element of the list and removes it from the list.
        Decrements the size."""
        pass
    
    def top(self):
        """Retrieves the head element of the list and removes it from the list.
        Sets 2nd element as the new head and decrements the size."""
        pass
        
    def reset(self):
        self.curr = self.head
        
        
class CircularList(LinkedList):
    """A Circular Linked List."""
    def __init__(self, l):
        super().__init__(l)
        
    def _populate(self, l):
        while self.size < len(l):
            if self.size == 0:
                newNode = ListNode(l[self.size])
                self.head = newNode
                self.curr = self.head
            else:
                newNode = self.curr.next
                self.curr = newNode
            try: newNode.next = ListNode(l[self.size+1])
            except IndexError:
                newNode.next = self.head
                self.curr = self.head
            self.size+=1
        
        
class DoubleLinkedList(LinkedList):
    """A Doubly-Linked List."""
    class ExtendedNode(ListNode):
        """Extended node (stores prev)"""
        def __init__(self, val):
            super().__init__(val)
            self.prev = None
    
    def __init__(self, l):
        super().__init__(l)
        
    def _populate(self, l):
        while self.size < len(l):
            if self.size == 0:
                newNode = self.ExtendedNode(l[self.size])
                self.head = newNode
                self.curr = self.head
            else:
                newNode = self.curr.next
                newNode.prev = self.curr
                self.curr = newNode
            try: newNode.next = self.ExtendedNode(l[self.size+1])
            except IndexError: self.tail = newNode
            self.size+=1
        self.reset()
    
    def traverse(self, n, reset=False):
        i = 0
        if reset and n > 0: self.reset()
        elif reset and n < 0: self.reset(True)
        try:
            while i < abs(n):
                if n > 0: self.curr = self.curr.next
                elif n < 0:  self.curr = self.curr.prev
                i+=1
            return self.curr.val
        except AttributeError:
            self.reset()
            return 'NIL'
        
    def reset(self, tail=False):
        if not tail: self.curr = self.head
        else: self.curr = self.tail
    
    
class Bst(object):
    """A Binary Search Tree"""
    def __init__(self, val=None):
        self._size, self._root = 0, None
        if val != None:
            if type(val) == int or type(val) == str: self.add(val)
            else:
                for i in val:
                    self.add(i)
                    
    def __del__(self):
        self._root = None
    
    def __len__(self): return self._size
    
    @property
    def root(self): return self._root
    @root.setter
    def root(self, node): self._root = node
    
    @property
    def height(self):
        """Returns the height of the tree"""
        if isinstance(self.root, TreeNode): return self.root.height
        else: return None
        
    def isEmpty(self): return self.root is None
        
    def add(self, val):
        """Adds an item to the tree recursively starting from the root"""
        if self.isEmpty():
            newNode = TreeNode(val)
            self.root, newNode._isroot = newNode, True
        if type(val) == type(self.root.val):
            self._add(val, self.root)
            self._size +=1
        else: raise TypeError\
        ('Value must be of type {}. Found {}'.format(type(self.root.val),type(val)))
    
    def _add(self, val, currNode):
        """Actual private recursive insert for non-root nodes"""
        if val > currNode:
            if currNode.rchild is None:
                currNode.rchild = TreeNode(val)
                if currNode.lchild is not None:
                    currNode.height = max(currNode.lchild.height, currNode.rchild.height) + 1
                else: currNode.height +=1
            else: self._add(val, currNode.rchild)
        elif val < currNode:
            if currNode.lchild is None:
                currNode.lchild = TreeNode(val)
                if currNode.rchild is not None:
                    currNode.height = max(currNode.lchild.height, currNode.rchild.height) + 1
                else: currNode.height +=1
            else: self._add(val, currNode.lchild)
    
    def __repr__(self):
        """Prints all tree node values Depth First in list form"""
        return str([node for node in self])
    
    def __iter__(self):
        if self.root is not None: return iter(self.root)
        else: return iter([])
                    
    def __contains__(self, val):
        print("searching for " + str(val) + " " + str(type(val)))
        if type(val) == type(self.root.val):
            return self._find(val, self.root)
        else:
            raise TypeError\
            ('Search value must be of type {}.'.format(type(self.root.val)))
    
    def __getitem__(self, key) -> TreeNode:
        """Retrieves a node. If the target node is not found
        or if the key is of the wrong type, we raise a KeyError."""
        try: return self._find(key, self.root)
        except TypeError: raise KeyError(str(key))
    
    def _find(self, val, currNode):
        """Recursive search. Returns the target node"""
        if currNode.val == val:
            return currNode
        elif val > currNode and currNode.rchild != None:
            return self._find(val, currNode.rchild)
        elif val < currNode and currNode.lchild != None:
            return self._find(val, currNode.lchild)
        else: raise KeyError(str(val))
    
    def _childandParent(self, val, currNode) -> tuple:
        """Recursive search. Returns the target node and its parent"""
        if val in currNode.children:
            return self[val], currNode
        elif val > currNode and currNode.rchild != None:
            return self._childandParent(val, currNode.rchild)
        elif val < currNode and currNode.lchild != None:
            return self._childandParent(val, currNode.lchild)
        else: return (self[val], currNode)
            
    def remove(self, val):
        """Removes a tree node containing a specified value
        should find the target node. If it is a leaf, destroy the leaf.
        if not, then travel down the left branch to find a node without a
        right child (max of the left sub-tree), then we reset the child node's
        children to that of the target node and redefine the target node as
        that child node. If there is no left sub-tree, we travel right and find
        a node with no left child (min of the right sub-tree) and perform substitution."""
        targetNode, parent = self._childandParent(val, self.root)
        if targetNode:
            if targetNode.isLeaf:
                if parent.lchild == targetNode: parent.lchild = None
                elif parent.rchild == targetNode: parent.rchild = None
                del targetNode
            
            else:
                if targetNode.isRoot: self.__del__()
                
                if targetNode != min(targetNode):
                    print("you are attemtping to remove the min")
                    subNode = min(targetNode)
                else: subNode = targetNode.rchild
                
                if parent.lchild == targetNode: parent.lchild = subNode
                elif parent.rchild == targetNode: parent.rchild = subNode
                
                if subNode not in targetNode.children:
                    subNode.lchild, subNode.rchild = targetNode.lchild, targetNode.rchild
                elif subNode == targetNode.lchild:
                    subNode.lchild, subNode.rchild = None, targetNode.rchild
                else:
                    subNode.lchild, subNode.rchild = targetNode.lchild, None
                    
                del targetNode
                
            bst._size -=1

if __name__ == '__main__':
    
    bst = Bst()
    bst2 = Bst()
    def fillTree(tree, num_elems=10, max_int=100000):
        from random import randint
        for _ in range(num_elems): tree.add(randint(0, max_int))
        return tree
    
    fillTree(bst)
    fillTree(bst2)