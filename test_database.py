from database_operations import save_rule, load_rules
import logging

# Sample rule and its corresponding AST (as a dictionary)
sample_rule = "age > 30 AND department = 'Sales'"
sample_ast = {
    "node_type": "operator",
    "value": "AND",
    "left": {"node_type": "operand", "value": "age > 30"},
    "right": {"node_type": "operand", "value": "department = 'Sales'"}
}

def test_database_operations():
    """Test saving and loading rules from the database."""
    try:
        # Step 1: Save the sample rule and AST to the database
        save_rule(sample_rule, sample_ast)
        print("Sample rule saved successfully.")

        # Step 2: Load and display all rules from the database
        rules = load_rules()
        print("Loaded Rules:")
        for rule in rules:
            print(f"Rule: {rule[0]}, AST JSON: {rule[1]}")

        # Assertions to ensure the rule is saved correctly
        assert len(rules) > 0, "No rules were loaded from the database."
        assert rules[0][0] == sample_rule, "Loaded rule does not match the saved rule."
        
        print("All assertions passed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    test_database_operations()
