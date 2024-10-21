import sqlite3
import json

def save_rule(rule_string, ast):
    """
    Save a rule and its AST to the database.

    Args:
        rule_string (str): The original rule string.
        ast (dict): The AST represented as a dictionary.
    """
    connection = sqlite3.connect('rules.db')
    cursor = connection.cursor()

    # Convert the AST to JSON for storage
    ast_json = json.dumps(ast)

    # Insert the rule into the database
    cursor.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", 
                   (rule_string, ast_json))

    connection.commit()
    connection.close()

    print("Rule saved successfully.")

def load_rules():
    """
    Load all rules from the database.

    Returns:
        list: A list of tuples (rule_string, ast_json).
    """
    connection = sqlite3.connect('rules.db')
    cursor = connection.cursor()

    cursor.execute("SELECT rule_string, ast_json FROM rules")
    rules = cursor.fetchall()

    connection.close()
    return rules
