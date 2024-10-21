class ASTNode:
    def __init__(self, node_type: str, value: str = None, left: 'ASTNode' = None, right: 'ASTNode' = None):
        """
        Initialize an AST Node.

        Args:
            node_type (str): "operator" (AND/OR) or "operand" (e.g., age > 30).
            value (str/int, optional): The value of the operand node or operator (AND/OR).
            left (ASTNode, optional): Reference to the left child node.
            right (ASTNode, optional): Reference to the right child node.
        """
        self.node_type = node_type  # "operator" or "operand"
        self.value = value  # AND/OR or comparison value
        self.left = left  # Left child node
        self.right = right  # Right child node

    def __repr__(self) -> str:
        """Returns a readable string representation of the node."""
        return f"ASTNode(type={self.node_type}, value={self.value}, left={self.left}, right={self.right})"

    def is_operator(self) -> bool:
        """Check if the node is an operator node."""
        return self.node_type == "operator"

    def is_operand(self) -> bool:
        """Check if the node is an operand node."""
        return self.node_type == "operand"
