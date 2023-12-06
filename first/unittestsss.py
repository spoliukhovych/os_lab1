import unittest
from unittest.mock import patch
from io import StringIO
from funcsss import CalculationManager


class TestCalculationManager(unittest.TestCase):
    def setUp(self):
        self.manager = CalculationManager()

    def assert_test_result(self, result, expected_output):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result()
            output = mock_stdout.getvalue().strip()
        self.assertIn(expected_output, output)

    def test_calculate_f(self):
        result = self.manager.calculate_f(3)
        self.assertEqual(result, 6)  # Приклад результата для x = 3

    def test_calculate_g(self):
        result = self.manager.calculate_g(4)
        self.assertEqual(result, 9)  # Приклад результата для x = 4

    def test_binary_operation(self):
        result = self.manager.binary_operation(2, 3)
        self.assertEqual(result, 6)  # Приклад бінарної операції

    def test_calculate_expression(self):
        x_value = 5
        self.assert_test_result(
            lambda: self.manager.calculate_expression(x_value),
            f"Result: {x_value * 2 * (x_value + 5)}"
        )

    def test_run_calculation(self):
        x_value = 5
        self.assert_test_result(
            lambda: self.manager.run_calculation(x_value),
            "Result:"
        )

if __name__ == '__main__':
    result = unittest.TextTestRunner(failfast=True).run(unittest.defaultTestLoader.loadTestsFromTestCase(TestCalculationManager))
    if not result.wasSuccessful():
        failed_tests = [test.id() for test, _ in result.failures + result.errors]
        print("\nFailed Tests:")
        for test_id in failed_tests:
            print(test_id)