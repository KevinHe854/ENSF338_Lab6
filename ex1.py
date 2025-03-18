# Question 4
# The second approach is faster because in the first way, we are always adding new elements to the right of the leaf node, resulting in a tree
# with n levels. In the worst-case scenario searching has a complexity of O(n). In the second approach the number of levels approaches log n, so 
# searching would have a complexity of O(log n).

import timeit
import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
    
def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode
    
def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

if __name__ == "__main__":
    tree1Setup = '''
from __main__ import Node
from __main__ import insert
from __main__ import search
vector = [i for i in range(1, 10001)]

tree1 = Node(vector[0])
for i in range(1, len(vector)):
    insert(vector[i], tree1)
    '''
    tree1Stmt= '''
for i in range(1, 10001):
    search(i, tree1)
    '''
    
    tree2Setup = '''
from __main__ import Node
from __main__ import insert
from __main__ import search
import random
vector = [i for i in range(1, 10001)]
random.shuffle(vector)

tree2 = Node(vector[0])
for i in range(1, len(vector)):
    insert(vector[i], tree2)
    '''
    tree2Stmt = '''
for i in range(1, 10001):
    search(i, tree2)
    '''
    
    totalTree1 = timeit.timeit(setup=tree1Setup, stmt=tree1Stmt, number=10)
    totalTree2 = timeit.timeit(setup=tree2Setup, stmt=tree2Stmt, number=10)
    
    print("Tree1 total time: {}\nTree1 average time: {}".format(totalTree1, totalTree1/10))
    print("Tree2 total time: {}\nTree2 average time: {}".format(totalTree2, totalTree2/10))
