import json
from flask import Flask, request, jsonify, abort
from database_operations import save_rule, load_rules
from backend.ast_evaluator import evaluate_rule

app = Flask(__name__)

@app.route('/')
def home():
    """
    Health check route to verify that the API is working.
    """
    return "Rule Engine API is working!"

@app.route('/rules', methods=['POST'])
def add_rule():
    """
    Add a new rule to the database.

    Request JSON Example:
    {
        "rule_string": "age > 30 AND department = 'Sales'",
        "ast": {
            "node_type": "operator",
            "value": "AND",
            "left": {"node_type": "operand", "value": "age > 30"},
            "right": {"node_type": "operand", "value": "department = 'Sales'"}
        }
    }
    """
    data = request.get_json()
    if not data or 'rule_string' not in data or 'ast' not in data:
        abort(400, "Invalid input. 'rule_string' and 'ast' are required.")

    save_rule(data['rule_string'], data['ast'])
    return jsonify({"message": "Rule added successfully"}), 201

@app.route('/rules', methods=['GET'])
def get_rules():
    """
    Retrieve all rules from the database.
    """
    rules = load_rules()
    if not rules:
        abort(404, "No rules found.")
    return jsonify({"rules": rules}), 200

@app.route('/evaluate', methods=['POST'])
def evaluate():
    """
    Evaluate a specific rule on provided data.

    Request Query Param: rule_id (int)
    Request JSON Example:
    {
        "data": {"age": 35, "department": "Sales"}
    }
    """
    rule_id = request.args.get('rule_id', type=int)
    if rule_id is None:
        abort(400, "rule_id query parameter is required.")

    data = request.get_json()
    if not data or 'data' not in data:
        abort(400, "Invalid input. 'data' is required.")

    rules = load_rules()
    print(rules)
    
    try:
        rule_string, ast_json = rules[rule_id - 1]
    except IndexError:
        abort(404, "Rule not found.")

    # Convert ast_json from a string to a dictionary
    ast_json = json.loads(ast_json)

    print(type(ast_json))  # Add this line
    print(ast_json)        # This will help you see the content
    result = evaluate_rule(ast_json, data['data'])
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)