def evaluate_rule(ast_node, data):
    """
    Recursively evaluate the given AST node against the provided data.

    Args:
        ast_node (ASTNode): The AST node to evaluate.
        data (dict): The data to evaluate the rule against.

    Returns:
        bool: True if the rule matches the data, otherwise False.
    """
    if ast_node.node_type == "operator":  # Use dot notation for accessing node attributes
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)

        if ast_node.value == "AND":
            return left_result and right_result
        elif ast_node.value == "OR":
            return left_result or right_result

    elif ast_node.node_type == "operand":
        # Parse the condition to extract attribute, operator, and value
        attribute, operator, value = parse_operand(ast_node.value)
        # Compare the extracted values using the provided data
        return compare(attribute, operator, value, data)

    raise ValueError("Invalid AST node type")



def parse_operand(condition):
    """
    Parse the operand node's condition (e.g., 'age > 30').

    Args:
        condition (str): A condition string like 'age > 30'.

    Returns:
        tuple: (attribute, operator, value) extracted from the condition.
    """
    parts = condition.split()
    attribute = parts[0]
    operator = parts[1]

    # Convert '=' to '=='
    if operator == '=':
        operator = '=='
        
    value = int(parts[2]) if parts[2].isdigit() else parts[2].strip("'")
    return attribute, operator, value

def compare(attribute, operator, value, data):
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
