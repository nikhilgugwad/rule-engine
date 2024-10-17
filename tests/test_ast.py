import unittest
from backend.ast_builder import create_rule_ast

class TestAST(unittest.TestCase):
    def test_create_rule_ast(self):
        node = create_rule_ast("age > 30")
        self.assertEqual(node.node_type, "operand")
        self.assertEqual(node.value, "age > 30")

if __name__ == '__main__':
    unittest.main()