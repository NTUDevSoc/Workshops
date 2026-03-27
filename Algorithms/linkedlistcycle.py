def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps
        
        if slow == fast:
            return True
            
    return False