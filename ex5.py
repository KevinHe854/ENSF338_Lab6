import random
import timeit

# Node class for Linked List implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Priority Queue using Linked List
class ListPriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def enqueue(self, value):
        # Create new node
        new_node = Node(value)
        
        # If queue is empty or new value is smaller than head
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            # Find position to insert
            current = self.head
            while current.next and current.next.value <= value:
                current = current.next
            
            # Insert new node
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.head is None:
            return None
        
        # Extract minimum value (head)
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        
        return value

# Priority Queue using Heap
class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def heapify(self, arr):
        self.heap = arr.copy()
        self.size = len(arr)
        
        # Heapify from bottom-up
        for i in range(self.size // 2 - 1, -1, -1):
            self._sift_down(i)
    
    def _sift_up(self, index):
        parent = (index - 1) // 2
        
        if index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._sift_up(parent)
    
    def _sift_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)
    
    def enqueue(self, value):
        self.heap.append(value)
        self.size += 1
        self._sift_up(self.size - 1)
    
    def dequeue(self):
        if self.size == 0:
            return None
        
        # Extract minimum value (root)
        value = self.heap[0]
        
        # Replace root with last element and remove last element
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        
        # Restore heap property
        if self.size > 0:
            self._sift_down(0)
        
        return value

# Function to test performance
def compare_performance(num_tasks=1000):
    # Generate random tasks (enqueue or dequeue)
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:  # 70% probability for enqueue
            tasks.append(("enqueue", random.randint(1, 1000)))
        else:  # 30% probability for dequeue
            tasks.append(("dequeue", None))
    
    # Test List Priority Queue
    list_queue = ListPriorityQueue()
    
    def run_list_queue():
        for operation, value in tasks:
            if operation == "enqueue":
                list_queue.enqueue(value)
            else:
                list_queue.dequeue()
    
    list_time = timeit.timeit(run_list_queue, number=10) / 10
    
    # Test Heap Priority Queue
    heap_queue = HeapPriorityQueue()
    
    def run_heap_queue():
        for operation, value in tasks:
            if operation == "enqueue":
                heap_queue.enqueue(value)
            else:
                heap_queue.dequeue()
    
    heap_time = timeit.timeit(run_heap_queue, number=10) / 10
    
    return {
        "list_total_time": list_time,
        "list_avg_time": list_time / num_tasks,
        "heap_total_time": heap_time,
        "heap_avg_time": heap_time / num_tasks
    }

def main():
    results = compare_performance()
    
    print("List Priority Queue:")
    print(f"  Total time: {results['list_total_time']:.6f} seconds")
    print(f"  Average time per task: {results['list_avg_time']:.8f} seconds")
    
    print("\nHeap Priority Queue:")
    print(f"  Total time: {results['heap_total_time']:.6f} seconds")
    print(f"  Average time per task: {results['heap_avg_time']:.8f} seconds")
    
    # Determine which is faster
    if results['heap_total_time'] < results['list_total_time']:
        print("\nHeap implementation is faster.")
    else:
        print("\nLinked List implementation is faster.")
    
    """
    Discussion:
    
    The heap implementation is generally faster than the linked list implementation for
    priority queue operations for the following reasons:
    
    1. Enqueue Operation:
       - List: O(n) time complexity in the worst case, as we need to traverse the list to find 
         the correct position to insert the new element.
       - Heap: O(log n) time complexity, as we only need to perform sift-up operations from 
         the inserted leaf to restore the heap property.
    
    2. Dequeue Operation:
       - List: O(1) time complexity, as we simply remove the head element.
       - Heap: O(log n) time complexity, as we need to perform sift-down operations to 
         restore the heap property after removing the root.
    
    3. Memory Locality:
       - The heap uses an array as its backing store, which has better memory locality than
         the linked nodes in a list implementation, leading to better cache performance.
    
    4. Practical Performance:
       - For small datasets, the linked list might perform better due to less overhead, but as
         the number of operations increases, the heap's better asymptotic complexity dominates.
    
    5. Use Case Considerations:
       - If our workload consists of more enqueues than dequeues (which is the case in our test - 70% 
         enqueues), the heap's advantage becomes more pronounced.
       - If our priority queue operations were heavily skewed toward dequeues, the linked list 
         might potentially perform better.
    
    The results confirm that for a typical mix of operations, the heap implementation provides
    better overall performance, especially as the size of the dataset grows, due to its
    O(log n) complexity for both operations compared to the linked list's O(n) enqueue operation.
    """

if __name__ == "__main__":
    main()
