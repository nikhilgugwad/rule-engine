from backend.ast import ASTNode
from typing import List

def create_rule_ast(rule_string: str) -> ASTNode:
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
    operand_node = ASTNode(node_type="operand", value=rule_string)  # Use full rule string
    return operand_node

def combine_rules(ast_nodes: List[ASTNode], operator: str) -> ASTNode:
    """
    Combine multiple AST nodes using a logical operator.

    Args:
        ast_nodes (List[ASTNode]): A list of ASTNode objects (sub-trees).
        operator (str): Logical operator to combine ('AND' or 'OR').

    Returns:
        ASTNode: The root node of the combined AST.
    """
    if not ast_nodes:
        raise ValueError("No AST nodes provided for combination.")
    if operator not in {"AND", "OR"}:
        raise ValueError("Operator must be 'AND' or 'OR'.")

    # Start combining nodes from the first one.
    combined_tree = ast_nodes[0]

    for node in ast_nodes[1:]:
        combined_tree = ASTNode(
            node_type="operator",
            value=operator,
            left=combined_tree,
            right=node
        )

    return combined_tree
