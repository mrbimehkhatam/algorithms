import unittest
import linear


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear.linear_search([3, 4, 6, 1, 4, 5], 6),  2)

    def test_linear_search_wrong_output(self):
        self.assertNotEqual(linear.linear_search([1, 23, 4, 5], 1), 1)

    def test_linear_search_empty_array(self):
        self.assertEqual(linear.linear_search([], 1) - 1)

    def test_linear_search_not_in_array(self):
        self.assertEqual(linear.linear_search([1, 3, 4, 5, 6], 7), -1)


if __name__ == "__main__":
    unittest.main()
