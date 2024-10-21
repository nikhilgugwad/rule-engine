import unittest
from backend.ast_builder import create_rule_ast, combine_rules
from backend.ast_evaluator import evaluate_rule

class TestRuleEvaluation(unittest.TestCase):
    def test_evaluate_single_rule1(self):
        """Test evaluation of a single rule where the condition is true."""
        rule = create_rule_ast("age > 30")
        data = {"age": 35}
        self.assertTrue(evaluate_rule(rule, data))

    def test_evaluate_combined_rule1(self):
        """Test evaluation of combined rules using AND."""
        rule1 = create_rule_ast("age > 30")
        rule2 = create_rule_ast("salary > 50000")
        combined_rule = combine_rules([rule1, rule2], "AND")

        data1 = {"age": 35, "salary": 60000}  # Both conditions true
        data2 = {"age": 28, "salary": 60000}  # First condition false

        self.assertTrue(evaluate_rule(combined_rule, data1))
        self.assertFalse(evaluate_rule(combined_rule, data2))

    def test_evaluate_single_rule2(self):
        """Test evaluation of a single rule with varying data."""
        rule = create_rule_ast("age > 30")
        data1 = {"age": 35}
        data2 = {"age": 25}
        self.assertTrue(evaluate_rule(rule, data1))
        self.assertFalse(evaluate_rule(rule, data2))

    def test_evaluate_combined_rule2(self):
        """Test evaluation of combined rules using AND with different departments."""
        rule1 = create_rule_ast("age > 30")
        rule2 = create_rule_ast("department = 'Sales'")
        combined_rule = combine_rules([rule1, rule2], "AND")

        data1 = {"age": 35, "department": "Sales"}       # Both conditions true
        data2 = {"age": 35, "department": "Marketing"}    # Second condition false

        self.assertTrue(evaluate_rule(combined_rule, data1))
        self.assertFalse(evaluate_rule(combined_rule, data2))

    def test_evaluate_complex_rule(self):
        """Test evaluation of a complex rule using AND and OR."""
        rule1 = create_rule_ast("age > 30")
        rule2 = create_rule_ast("salary > 50000")
        rule3 = create_rule_ast("department = 'Sales'")

        # Combine using AND and OR
        combined_rule = combine_rules([rule1, rule2], "AND")
        final_rule = combine_rules([combined_rule, rule3], "OR")

        data1 = {"age": 35, "salary": 60000, "department": "Marketing"}  # AND part true, OR true
        data2 = {"age": 25, "salary": 60000, "department": "Sales"}       # AND part false, OR true

        self.assertTrue(evaluate_rule(final_rule, data1))
        self.assertTrue(evaluate_rule(final_rule, data2))

    def test_evaluate_missing_attribute(self):
        """Test evaluation when an expected attribute is missing in data."""
        rule = create_rule_ast("age > 30")
        data = {}  # No attributes provided
        with self.assertRaises(KeyError):
            evaluate_rule(rule, data)

    def test_evaluate_unsupported_operator(self):
        """Test evaluation with an unsupported operator should raise ValueError."""
        rule = create_rule_ast("age ? 30")  # Invalid operator
        data = {"age": 35}
        with self.assertRaises(ValueError):
            evaluate_rule(rule, data)

if __name__ == '__main__':
    unittest.main()
