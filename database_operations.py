import sqlite3
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def initialize_database():
    """Create the rules table if it doesn't exist."""
    with sqlite3.connect('rules.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rule_string TEXT NOT NULL,
                ast_json TEXT NOT NULL
            )
        ''')
        connection.commit()

def save_rule(rule_string, ast):
    """
    Save a rule and its AST to the database.

    Args:
        rule_string (str): The original rule string.
        ast (dict): The AST represented as a dictionary.
    """
    try:
        ast_json = json.dumps(ast)  # Convert the AST to JSON for storage
        with sqlite3.connect('rules.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", 
                           (rule_string, ast_json))
            connection.commit()
        logging.info("Rule saved successfully.")

    except sqlite3.Error as e:
        logging.error(f"An error occurred while saving the rule: {e}")

def load_rules():
    """
    Load all rules from the database.

    Returns:
        list: A list of tuples (rule_string, ast_json).
    """
    try:
        with sqlite3.connect('rules.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT rule_string, ast_json FROM rules")
            rules = cursor.fetchall()
        return rules

    except sqlite3.Error as e:
        logging.error(f"An error occurred while loading rules: {e}")
        return []
