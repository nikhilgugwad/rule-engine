# Rule Engine API Documentation

## Project Overview
This project is a **Rule Engine API** that allows users to define and evaluate rules based on various conditions. The rules can be combined using logical operators (AND, OR) and evaluated against given data.

### Key Features
- Add rules with their corresponding AST (Abstract Syntax Tree).
- Evaluate rules against provided data.
- Store rules persistently in a SQLite database.

## Installation Instructions

### Prerequisites
- Python 3.11.9
- Flask 3.0.3
- SQLite3 (comes pre-installed with Python)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/nikhilgugwad/rule-engine.git
   cd rule-engine-api
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python database_setup.py
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. The API should now be running at `http://127.0.0.1:5000/`.

## Usage Instructions

### API Endpoints

#### 1. Health Check
- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Verify that the API is working.

**Example Request**:
```bash
curl -X GET http://127.0.0.1:5000/
```

**Example Response**:
```json
"Rule Engine API is working!"
```

---

#### 2. Add Rule
- **Endpoint**: `/rules`
- **Method**: `POST`
- **Description**: Add a new rule to the database.

**Request Payload**:
```json
{
    "rule_string": "age > 30 AND department = 'Sales'",
    "ast": {
        "node_type": "operator",
        "value": "AND",
        "left": {"node_type": "operand", "value": "age > 30"},
        "right": {"node_type": "operand", "value": "department = 'Sales'"}
    }
}
```

**Example Request**:
```bash
curl -X POST http://127.0.0.1:5000/rules -H "Content-Type: application/json" -d '{
    "rule_string": "age > 30 AND department = 'Sales'",
    "ast": {
        "node_type": "operator",
        "value": "AND",
        "left": {"node_type": "operand", "value": "age > 30"},
        "right": {"node_type": "operand", "value": "department = 'Sales'"}
    }
}'
```

**Example Response**:
```json
{
    "message": "Rule added successfully"
}
```

---

#### 3. Get Rules
- **Endpoint**: `/rules`
- **Method**: `GET`
- **Description**: Retrieve all rules from the database.

**Example Request**:
```bash
curl -X GET http://127.0.0.1:5000/rules
```

**Example Response**:
```json
{
    "rules": [
        {
            "rule_string": "age > 30 AND department = 'Sales'",
            "ast_json": "{\"node_type\": \"operator\", \"value\": \"AND\", \"left\": {\"node_type\": \"operand\", \"value\": \"age > 30\"}, \"right\": {\"node_type\": \"operand\", \"value\": \"department = 'Sales'\"}}"
        }
    ]
}
```

---

#### 4. Evaluate Rule
- **Endpoint**: `/evaluate`
- **Method**: `POST`
- **Description**: Evaluate a specific rule on provided data.

**Query Parameter**: 
- `rule_id` (int): The ID of the rule to evaluate.

**Request Payload**:
```json
{
    "data": {"age": 35, "department": "Sales"}
}
```

**Example Request**:
```bash
curl -X POST http://127.0.0.1:5000/evaluate?rule_id=1 -H "Content-Type: application/json" -d '{
    "data": {"age": 35, "department": "Sales"}
}'
```

**Example Response**:
```json
{
    "result": true
}
```

## Testing Instructions

### Testing Framework
This project uses the `unittest` framework for testing.

### Running Tests
To run the tests in this project, follow these steps:

1. **Set Up the Database**:
   Ensure that the database is set up by running the `database_setup.py` script to create the `rules.db` file.

   ```bash
   python database_setup.py
   ```

2. **Run the Tests**:
   You can run all tests using the following command:

   ```bash
   python -m unittest discover -s tests
   ```

   Alternatively, to run a specific test file, use:

   ```bash
   python -m unittest tests/test_ast_evaluator.py
   ```

### Test Structure
The tests are organized in the `tests` directory, which includes the following test files:

- **test_ast_evaluator.py**: Contains unit tests for the AST evaluation logic.
- **test_database.py**: Tests for database operations, ensuring rules can be saved and loaded correctly.
- **test_app.py**: Tests for the Flask application endpoints to verify correct API behavior.

Each test file uses the `unittest` framework to define test cases and assertions.

## Contribution Guidelines

We welcome contributions to this project! Please follow the guidelines below to help us maintain a high-quality codebase.

### How to Contribute

1. **Fork the Repository**:
   - Click the "Fork" button in the top-right corner of the repository to create your copy of the project.

2. **Create a Feature Branch**:
   - Create a new branch for your feature or bug fix. Use a descriptive name for your branch.
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**:
   - Make your changes, ensuring that you follow the coding standards and conventions used in the project.

4. **Commit Your Changes**:
   - Commit your changes with a clear and concise commit message.
   ```bash
   git commit -m "Add your message here"
   ```

5. **Push to Your Fork**:
   - Push your changes to your forked repository.
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Go to the original repository and create a pull request from your feature branch.
   - Provide a clear description of your changes and why they should be merged.

