"""
=======================================================================
DATA STRUCTURES FOR Internships/Placements/Graduate Roles
=======================================================================

This script outlines the core data structures expected in technical 
interviews for graduate-level roles. 

For each data structure, we provide:
1. The formal Computer Science name.
2. The Python implementation.
3. Key features & Time/Space Complexity.
4. A practical usage example.
=======================================================================
"""

from collections import deque
import heapq

# ---------------------------------------------------------------------
# 1. DYNAMIC ARRAYS
# Python Implementation: list
# ---------------------------------------------------------------------
"""
Key Features:
- Elements are stored in contiguous memory locations.
- Python's 'list' automatically resizes itself under the hood (dynamic).
- O(1) time complexity for indexing and appending to the end.
- O(n) time complexity for inserting/deleting at the beginning or middle.

Common Usage:
Storing ordered sequences, iterating over items, and returning results.
"""
print("--- Dynamic Arrays ---")
# Initialise an array (list)
nums = [1, 2, 3]

# Appending to the end is an O(1) operation
nums.append(4) 

# Accessing an element by index is O(1)
first_element = nums[0] 

# Inserting at index 0 is O(n) because all other elements must shift
nums.insert(0, 99) 
print(f"Dynamic Array after operations: {nums}\n")


# ---------------------------------------------------------------------
# 2. HASH MAPS (Hash Tables)
# Python Implementation: dict (Dictionary)
# ---------------------------------------------------------------------
"""
Key Features:
- Stores data in key-value pairs.
- Uses a hashing function to compute an index for fast data retrieval.
- O(1) average time complexity for insertions, deletions, and lookups.
- Does not guarantee order in older versions, but Python 3.7+ maintains 
  insertion order.

Common Usage:
Counting frequencies, caching/memoisation, and O(1) lookups (e.g., the 
Two Sum problem).
"""
print("--- Hash Maps ---")
# Initialise a hash map (dictionary)
seen_map = {}

# O(1) insertion
seen_map["apple"] = 5
seen_map["banana"] = 2

# O(1) lookup
if "apple" in seen_map:
    print(f"We have {seen_map['apple']} apples.")

# Practical example: Frequency counter
word = "interview"
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1
print(f"Character frequencies in '{word}': {freq}\n")


# ---------------------------------------------------------------------
# 3. HASH SETS
# Python Implementation: set
# ---------------------------------------------------------------------
"""
Key Features:
- A collection of unique elements (no duplicates allowed).
- Under the hood, it operates similarly to a Hash Map but without values.
- O(1) average time complexity for adding, removing, and checking membership.

Common Usage:
Removing duplicates from an array, finding intersections, and fast 
membership testing.
"""
print("--- Hash Sets ---")
# Initialise sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Union (elements in either): {a | b}")
print(f"Intersection (elements in both): {a & b}")

# Finding duplicates in a list
raw_data = [1, 2, 2, 3, 4, 4, 5]
seen = set()
duplicates = set()

for num in raw_data:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
        
print(f"Duplicates found: {duplicates}\n")


# ---------------------------------------------------------------------
# 4. STACKS
# Python Implementation: list (Using append and pop)
# ---------------------------------------------------------------------
"""
Key Features:
- Operates on a Last-In-First-Out (LIFO) principle.
- The last element added is the first one to be removed.
- O(1) time complexity for pushing (append) and popping (pop) at the end.

Common Usage:
Validating brackets (e.g., matching parentheses), undo mechanisms, and 
Depth-First Search (DFS) algorithms.
"""
print("--- Stacks ---")
stack = []

# Push elements (LIFO behaviour)
stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")

# Pop the most recently added element
last_page = stack.pop()
print(f"Popped from stack: {last_page}")
print(f"Current stack state: {stack}\n")


# ---------------------------------------------------------------------
# 5. QUEUES
# Python Implementation: collections.deque (Double-Ended Queue)
# ---------------------------------------------------------------------
"""
Key Features:
- Operates on a First-In-First-Out (FIFO) principle.
- Using a standard Python list for a queue is inefficient (O(n) for pop(0)).
- 'deque' is implemented as a doubly linked list under the hood, allowing 
  O(1) appends and pops from both ends.

Common Usage:
Breadth-First Search (BFS), task scheduling, and buffering.
"""
print("--- Queues ---")
# Initialise a queue using deque
q = deque()

# Enqueue (add to the back)
q.append("Customer A")
q.append("Customer B")
q.append("Customer C")

# Dequeue (remove from the front)
served = q.popleft()
print(f"Served: {served}")
print(f"Queue remaining: {list(q)}\n")


# ---------------------------------------------------------------------
# 6. HEAPS (Priority Queues)
# Python Implementation: heapq module (used on standard lists)
# ---------------------------------------------------------------------
"""
Key Features:
- A binary tree structure where the parent node is always smaller (Min-Heap)
  or larger (Max-Heap) than its children.
- Python's 'heapq' only implements Min-Heaps by default.
- O(log n) time complexity for insertion and extraction.
- O(1) time complexity to get the minimum element (arr[0]).

Common Usage:
Finding the "Kth largest/smallest" element, Dijkstra's algorithm, and 
scheduling tasks by priority.
"""
print("--- Heaps ---")
# Start with a standard list
min_heap = [5, 1, 8, 3]

# Convert the list into a heap in-place - O(n)
heapq.heapify(min_heap)
print(f"Heapified list: {min_heap}")

# Push a new element - O(log n)
heapq.heappush(min_heap, 2)

# Pop the smallest element - O(log n)
smallest = heapq.heappop(min_heap)
print(f"Popped smallest element: {smallest}")
print(f"Heap after popping: {min_heap}\n")


# ---------------------------------------------------------------------
# 7. LINKED LISTS
# Python Implementation: Custom Class
# ---------------------------------------------------------------------
"""
Key Features:
- Elements (Nodes) are stored in non-contiguous memory.
- Each node holds a value and a reference (pointer) to the next node.
- O(1) insertions/deletions if you already have the node reference.
- O(n) lookup time (you must traverse from the 'head').

Common Usage:
Implementing queues or stacks under the hood, cycle detection, and 
managing dynamic data where size is constantly fluctuating.
"""
print("--- Linked Lists ---")
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

# Initialise nodes
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Traverse the linked list
current = head
values = []
while current:
    values.append(current.val)
    current = current.next
print(f"Linked List values: {values}\n")


# ---------------------------------------------------------------------
# 8. TREES (Binary Trees)
# Python Implementation: Custom Class
# ---------------------------------------------------------------------
"""
Key Features:
- Hierarchical data structure with a root value and subtrees of children.
- In a Binary Tree, each node has at most two children (left and right).
- Binary Search Trees (BST) keep smaller values on the left and larger on the right.
- Traversals (Inorder, Preorder, Postorder) take O(n) time.

Common Usage:
Representing hierarchical data, fast searching/sorting (BST), and Tries 
for autocomplete features.
"""
print("--- Trees ---")
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build a simple tree
#       10
#      /  \
#     5    15
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print(f"Root: {root.val}, Left Child: {root.left.val}, Right Child: {root.right.val}\n")


# ---------------------------------------------------------------------
# 9. GRAPHS
# Python Implementation: Hash Map of Lists (Adjacency List)
# ---------------------------------------------------------------------
"""
Key Features:
- A collection of Nodes (vertices) and Edges connecting them.
- Can be directed or undirected, weighted or unweighted.
- Usually represented using an Adjacency Matrix (2D array) or an 
  Adjacency List (Hash Map of lists). Adjacency List is preferred for 
  sparse graphs to save space.

Common Usage:
Social networks (mutual friends), routing algorithms (Google Maps), and 
dependency resolution.
"""
print("--- Graphs (Adjacency List) ---")
# Representing an undirected graph where A is connected to B and C
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

node = "A"
print(f"Neighbours of node {node}: {graph[node]}")