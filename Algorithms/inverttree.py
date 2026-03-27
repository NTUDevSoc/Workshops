def invertTree(root):
    if not root:
        return None

    # Swap the children
    root.left, root.right = root.right, root.left

    # Recurse
    invertTree(root.left)
    invertTree(root.right)

    return root