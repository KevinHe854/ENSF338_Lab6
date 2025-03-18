# Question 4
# The array implementation of binary search is faster than the BST implementation of search. Both searches have complexity of O(log n). The 
# difference is that the array is perfectly split in half during binary search each time, while the BST isn't perfectly split in half because the 
# nodes were inserted in a random order. Due to this, the BST search will take more steps than array binary search on average.

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

def binary_search(num, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if num == arr[mid]:
            return mid
        elif num < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == "__main__":    
    BSTSetup = '''
from __main__ import Node
from __main__ import insert
from __main__ import search
import random
vector = [i for i in range(1, 10001)]
random.shuffle(vector)

BST = Node(vector[0])
for i in range(1, len(vector)):
    insert(vector[i], BST)
    '''
    BSTStmt = '''
for i in range(1, 10001):
    search(i, BST)
    '''
    
    ArraySetup = '''
from __main__ import binary_search
vector = [i for i in range(1, 10001)]
    '''
    ArrayStmt = '''
for i in range(1, 11):
    binary_search(i, vector)
    '''
    
    BSTTime = timeit.timeit(setup=BSTSetup, stmt=BSTStmt, number=10)
    ArrayTime = timeit.timeit(setup=ArraySetup, stmt=ArrayStmt, number=10)
    
    print("BST total time: {}\nBST average time: {}".format(BSTTime, BSTTime/10))
    print("Array total time: {}\nArray average time: {}".format(ArrayTime, ArrayTime/10))
