class ASTNode:
    def __init__(self, node_type, value=None, left=None, right=None):
        """
        Initialize an AST Node.

        Args:
            node_type (str): "operator" (AND/OR) or "operand" (e.g., age > 30).
            value (str/int): The value of the operand node or operator (AND/OR).
            left (ASTNode): Reference to the left child node.
            right (ASTNode): Reference to the right child node.
        """
        self.node_type = node_type  # "operator" or "operand"
        self.value = value  # AND/OR or comparison value
        self.left = left  # Left child node
        self.right = right  # Right child node

    def __repr__(self):
        """Returns a readable string representation of the node."""
        return f"ASTNode(type={self.node_type}, value={self.value})"
