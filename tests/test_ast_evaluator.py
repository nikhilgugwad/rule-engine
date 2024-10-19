import unittest
from backend.ast_builder import create_rule_ast, combine_rules
from backend.ast_evaluator import evaluate_rule

class TestRuleEvaluation(unittest.TestCase):
    def test_evaluate_single_rule(self):
        rule = create_rule_ast("age > 30")
        data = {"age": 35}
        self.assertTrue(evaluate_rule(rule, data))

    def test_evaluate_combined_rule(self):
        rule1 = create_rule_ast("age > 30")
        rule2 = create_rule_ast("salary > 50000")
        combined_rule = combine_rules([rule1, rule2], "AND")

        data1 = {"age": 35, "salary": 60000}
        data2 = {"age": 28, "salary": 60000}

        self.assertTrue(evaluate_rule(combined_rule, data1))
        self.assertFalse(evaluate_rule(combined_rule, data2))

if __name__ == '__main__':
    unittest.main()
