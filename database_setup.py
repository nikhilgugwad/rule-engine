import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def setup_database():
    """Set up the SQLite database and create the rules table."""
    try:
        # Connect to SQLite (This creates a file 'rules.db' if it doesn't exist)
        connection = sqlite3.connect('rules.db')
        cursor = connection.cursor()

        # Create the table to store rules with columns for ID, rule string, and AST JSON
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rule_string TEXT NOT NULL,
                ast_json TEXT NOT NULL
            )
        """)

        # Commit changes and close the connection
        connection.commit()
        logging.info("Database and table setup completed successfully.")

    except sqlite3.Error as e:
        logging.error(f"An error occurred while setting up the database: {e}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    setup_database()
