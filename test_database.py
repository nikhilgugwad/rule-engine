from database_operations import save_rule, load_rules

# Sample rule and its corresponding AST (as a dictionary)
sample_rule = "age > 30 AND department = 'Sales'"
sample_ast = {
    "node_type": "operator",
    "value": "AND",
    "left": {"node_type": "operand", "value": "age > 30"},
    "right": {"node_type": "operand", "value": "department = 'Sales'"}
}

# Step 1: Save the sample rule and AST to the database
save_rule(sample_rule, sample_ast)

# Step 2: Load and display all rules from the database
rules = load_rules()
print("Loaded Rules:")
for rule in rules:
    print(f"Rule: {rule[0]}, AST JSON: {rule[1]}")
