from backend.ast import ASTNode

def create_rule_ast(rule_string):
    """
    Create an AST from a rule string.

    Args:
        rule_string (str): A rule string like 'age > 30 AND salary > 50000'.

    Returns:
        ASTNode: Root node of the generated AST.
    """
    tokens = rule_string.split()  # Split rule by spaces
    if len(tokens) != 3:
        raise ValueError("Invalid rule format. Expected format: 'attribute operator value'.")

    # Create operand node (e.g., age > 30)
    operand_node = ASTNode(node_type="operand", value=f"{tokens[0]} {tokens[1]} {tokens[2]}")
    return operand_node
