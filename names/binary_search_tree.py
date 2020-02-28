class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # each object should be its own BST
        bst_value = BinarySearchTree(value)
        # if lower than current node
        if self.value >= value:
            # if it doesnt have a child, this value becomes child
            if not self.left:
                self.left = bst_value
            else:
                # recursion with the left child
                return self.left.insert(value)
        # if greater than current node
        elif self.value < value:
            # if it doesnt have child, this value becomes child
            if not self.right:
                self.right = bst_value
            else:
                # recursion with the right child
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case - found target:
        if self.value == target:
            # return true
            return True

        # if current value is higher than target
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
        return False
