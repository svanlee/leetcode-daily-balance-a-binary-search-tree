# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(n), where n is the number of nodes in the tree
    # Space Complexity: O(n), where n is the number of nodes in the tree
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Create a list to store the nodes of the tree
        nodes = []
        
        # Perform an in-order traversal of the tree to store the nodes in the list
        self.inorder(root, nodes)
        
        # Build a balanced binary search tree from the list of nodes
        return self.buildBST(nodes, 0, len(nodes)-1)


    # Perform an in-order traversal of the tree and store the nodes in the list
    def inorder(self, root: TreeNode, nodes):
        if not root:
            return 
        # Traverse the left subtree
        self.inorder(root.left, nodes)
        # Add the current node to the list
        nodes.append(root)
        # Traverse the right subtree
        self.inorder(root.right, nodes)

    # Build a balanced binary search tree from the list of nodes
    def buildBST(self, nodes, left, right) -> TreeNode:
        if left > right:
            return None
        
        # Calculate the middle index of the list
        mid = (left + right)//2
        
        # Create a new node with the middle element of the list
        node = nodes[mid]
        
        # Recursively build the left and right subtrees
        node.left = self.buildBST(nodes, left, mid-1)
        node.right = self.buildBST(nodes, mid+1, right)
        
        # Return the root of the balanced binary search tree
        return node