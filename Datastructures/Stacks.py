def is_valid_parentheses(s):
    """
    Checks if a string of parentheses is valid.
    Example: "()[]{}" -> True
    Example: "([)]" -> False
    """
    stack = []
    # A map to store the closing-to-opening bracket pairs
    close_to_open_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        # If it's a closing bracket
        if char in close_to_open_map:
            # Check if stack is not empty AND
            # the top of the stack is the matching opening bracket
            if stack and stack[-1] == close_to_open_map[char]:
                stack.pop()  # It's a valid pair, pop it
            else:
                return False # Mismatch or stack is empty
        
        # If it's an opening bracket, just push it onto the stack
        else:
            stack.append(char)
    
    # If the stack is empty, all brackets were matched.
    return not stack

# Example
print(f"Is '()[]{{}}' valid? {is_valid_parentheses('()[]{}')}")
print(f"Is '([)]' valid? {is_valid_parentheses('([)]')}")

# time and space complexity 0(n)