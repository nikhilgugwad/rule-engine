import unittest
from backend.ast_builder import create_rule_ast, combine_rules

class TestASTCombination(unittest.TestCase):
    def test_combine_rules(self):
        node1 = create_rule_ast("age > 30")
        node2 = create_rule_ast("salary > 50000")
        combined = combine_rules([node1, node2], "AND")

        # Verify combined node properties
        self.assertEqual(combined.node_type, "operator")
        self.assertEqual(combined.value, "AND")
        self.assertEqual(combined.left.value, "age > 30")
        self.assertEqual(combined.right.value, "salary > 50000")

    def test_combine_additional_rules1(self):
        node1 = create_rule_ast("age > 30")
        node2 = create_rule_ast("salary > 50000")
        combined_or = combine_rules([node1, node2], "OR")

        # Verify combined OR node properties
        self.assertEqual(combined_or.node_type, "operator")
        self.assertEqual(combined_or.value, "OR")
        self.assertEqual(combined_or.left.value, "age > 30")
        self.assertEqual(combined_or.right.value, "salary > 50000")

    def test_combine_additional_rules2(self):
        node1 = create_rule_ast("age > 30")
        node2 = create_rule_ast("salary > 50000")
        
        # Combine the rules using AND
        combined = combine_rules([node1, node2], "AND")

        # Verify the properties of the combined node
        self.assertEqual(combined.left.value, "age > 30")
        self.assertEqual(combined.right.value, "salary > 50000")
        self.assertEqual(combined.value, "AND")

    def test_combine_no_nodes(self):
        """Test combining with no AST nodes should raise ValueError."""
        with self.assertRaises(ValueError):
            combine_rules([], "AND")

    def test_combine_invalid_operator(self):
        """Test combining with an invalid operator should raise ValueError."""
        node1 = create_rule_ast("age > 30")
        with self.assertRaises(ValueError):
            combine_rules([node1], "INVALID")

if __name__ == '__main__':
    unittest.main()
