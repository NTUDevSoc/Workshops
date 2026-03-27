from collections import deque

# 1. Initialise a queue
q = deque()

# 2. Add items (enqueue)
q.append('a')
q.append('b')
q.append('c')
print(f"Queue after appends: {q}")

# 3. Remove items (dequeue)
first_item = q.popleft()
print(f"Removed item: {first_item}")
print(f"Queue after popleft: {q}")

# 4. Check if empty
if q:
    print("Queue is not empty")

# used for breadth first search