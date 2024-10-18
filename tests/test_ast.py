import unittest
from backend.ast_builder import create_rule_ast, combine_rules

class TestAST(unittest.TestCase):
    def test_create_rule_ast(self):
        node = create_rule_ast("age > 30")
        self.assertEqual(node.node_type, "operand")
        self.assertEqual(node.value, "age > 30")

class TestASTCombination(unittest.TestCase):
    def test_combine_rules(self):
        node1 = create_rule_ast("age > 30")
        node2 = create_rule_ast("salary > 50000")
        combined = combine_rules([node1, node2], "AND")

        self.assertEqual(combined.node_type, "operator")
        self.assertEqual(combined.value, "AND")
        self.assertEqual(combined.left.value, "age > 30")
        self.assertEqual(combined.right.value, "salary > 50000")

if __name__ == '__main__':
    unittest.main()