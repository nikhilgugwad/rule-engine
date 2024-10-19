def evaluate_rule(ast_node, data):
    """
    Evaluate the AST node against the provided data.

    Args:
        ast_node (ASTNode): The root node of the AST representing the rule.
        data (dict): Dictionary containing attributes (e.g., {"age": 35, "department": "Sales"}).

    Returns:
        bool: True if the data satisfies the rule, False otherwise.
    """
    if ast_node.node_type == "operator":
        if ast_node.value == "AND":
            return evaluate_rule(ast_node.left, data) and evaluate_rule(ast_node.right, data)
        elif ast_node.value == "OR":
            return evaluate_rule(ast_node.left, data) or evaluate_rule(ast_node.right, data)

    elif ast_node.node_type == "operand":
        attribute, operator, value = parse_operand(ast_node.value)
        return compare(attribute, operator, value, data)

    else:
        raise ValueError(f"Invalid node type: {ast_node.node_type}")

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
