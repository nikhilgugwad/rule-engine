import sqlite3

# Step 1: Connect to SQLite (This creates a file 'rules.db' if it doesn't exist)
connection = sqlite3.connect('rules.db')

# Step 2: Create a cursor to execute SQL commands
cursor = connection.cursor()

# Step 3: Create the table to store rules with columns for ID, rule string, and AST JSON
cursor.execute("""
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_string TEXT NOT NULL,
        ast_json TEXT NOT NULL
    )
""")

# Step 4: Commit changes and close the connection
connection.commit()
connection.close()

print("Database and table setup completed successfully.")
