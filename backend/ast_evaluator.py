from typing import Any, Dict, Tuple

def evaluate_rule(ast_node, data: Dict[str, Any]) -> bool:
    """
    Recursively evaluate the given AST node against the provided data.

    Args:
        ast_node (ASTNode): The AST node to evaluate.
        data (dict): The data to evaluate the rule against.

    Returns:
        bool: True if the rule matches the data, otherwise False.
    """
    if ast_node.node_type == "operator":
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)

        return (left_result and right_result) if ast_node.value == "AND" else \
               (left_result or right_result) if ast_node.value == "OR" else \
               ValueError("Unsupported operator")

    elif ast_node.node_type == "operand":
        # Parse the condition to extract attribute, operator, and value
        attribute, operator, value = parse_operand(ast_node.value)
        # Compare the extracted values using the provided data
        return compare(attribute, operator, value, data)

    raise ValueError("Invalid AST node type")

def parse_operand(condition: str) -> Tuple[str, str, Any]:
    """
    Parse the operand node's condition (e.g., 'age > 30').

    Args:
        condition (str): A condition string like 'age > 30'.

    Returns:
        tuple: (attribute, operator, value) extracted from the condition.
    """
    parts = condition.split()
    if len(parts) != 3:
        raise ValueError("Invalid operand condition format. Expected format: 'attribute operator value'.")

    attribute, operator = parts[0], parts[1]
    # Convert '=' to '=='
    operator = '==' if operator == '=' else operator
    # Determine the value type
    value = int(parts[2]) if parts[2].isdigit() else parts[2].strip("'")

    return attribute, operator, value

def compare(attribute: str, operator: str, value: Any, data: Dict[str, Any]) -> bool:
    """
    Compare the attribute from the data with the given value using the operator.

    Args:
        attribute (str): The attribute name (e.g., 'age').
        operator (str): Comparison operator (e.g., '>', '==').
        value (Any): The value to compare against.
        data (dict): Input data containing the attribute.

    Returns:
        bool: True if the comparison holds, False otherwise.
    """
    if attribute not in data:
        raise KeyError(f"Attribute '{attribute}' not found in data.")

    attr_value = data[attribute]

    if operator == ">":
        return attr_value > value
    elif operator == "<":
        return attr_value < value
    elif operator == "==":
        return attr_value == value
    elif operator == "!=":
        return attr_value != value
    else:
        raise ValueError(f"Unsupported operator: {operator}")
