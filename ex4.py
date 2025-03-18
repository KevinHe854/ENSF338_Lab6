import heapq
from random import shuffle

class heap: # this is a min heap
    def __init__(self, array):
        self.heap = array
        self.heapify(self.heap)
    
    def heapify(self, heap):
        heapq.heapify(heap)
    
    def enqueue(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1
        while True:
            parent = (i - 1) // 2
            if parent < len(self.heap) and self.heap[i] < self.heap[parent]:
                temp = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = temp
                i = parent
            else:
                break
    
    def dequeue(self):
        root = self.heap[0]
        
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            if right < len(self.heap):
                if self.heap[left] <= self.heap[right]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[left]
                    self.heap[left] = temp
                    i = left
                else:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[right]
                    self.heap[right] = temp
                    i = right
                continue
            break
        
        return root

if __name__ == "__main__":
    list = [1, 3, 5, 78, 21, 45]
    sortedHeap = heap(list)
    print(sortedHeap.heap)
    sortedHeap.enqueue(4)
    print(sortedHeap.heap)
    sortedHeap.dequeue()
    print(sortedHeap.heap)
    
    emptyHeap = heap([])
    print(emptyHeap.heap)
    emptyHeap.enqueue(1)
    print(emptyHeap.heap)
    emptyHeap.dequeue()
    print(emptyHeap.heap)
    
    list = [i for i in range(1, 101)]
    shuffle(list)
    randomHeap = heap(list)
    print(randomHeap.heap)
    randomHeap.enqueue(101)
    print(randomHeap.heap)
    randomHeap.dequeue()
    print(randomHeap.heap)