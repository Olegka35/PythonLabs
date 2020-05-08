import unittest
from polynomial import Polynomial


class PolynomialTest(unittest.TestCase):

    # INIT TESTS

    def test_init_by_list(self):
        self.assertEqual([1, 2, -4], Polynomial([1, 2, -4]).coeffs)

    def test_init_by_tuple(self):
        self.assertEqual([1, 2, -4], Polynomial((1, 2, -4)).coeffs)

    def test_init_with_extra_zeros(self):
        self.assertEqual([1, 2, -4], Polynomial((0, 0, 0, 1, 2, -4)).coeffs)

    def test_init_by_zero(self):
        self.assertEqual([0], Polynomial([0]).coeffs)

    def test_init_by_zeros(self):
        self.assertEqual([0], Polynomial((0, 0, 0)).coeffs)

    def test_init_fails_on_empty_list(self):
        with self.assertRaises(AttributeError):
            Polynomial([])

    def test_init_fails_on_incorrect_data(self):
        with self.assertRaises(TypeError):
            Polynomial(1)

    def test_init_fails_on_incorrect_coef_type(self):
        with self.assertRaises(TypeError):
            Polynomial(['42453', '24'])

    def test_init_fails_on_incorrect_coef_type2(self):
        with self.assertRaises(TypeError):
            Polynomial([2.0, 6.1])

    def test_init_by_polynomial(self):
        pol1 = Polynomial([1, 2, -4])
        pol2 = Polynomial(pol1)
        self.assertEqual(pol1.coeffs, pol2.coeffs)

    # ADD TESTS

    def test_add_with_number(self):
        self.assertEqual(Polynomial([1, 2, -3]), Polynomial([1, 2, -4]) + 1)

    def test_add_with_number2(self):
        self.assertEqual(Polynomial([1, 2, -1]), 3 + Polynomial([1, 2, -4]))

    def test_add_with_zero(self):
        self.assertEqual(Polynomial([1, 2, -4]), Polynomial([1, 2, -4]) + 0)

    def test_add_fail_incorrect_type(self):
        with self.assertRaises(TypeError):
            'test' + Polynomial([1, 2, -4])

    def test_add_with_polynomial(self):
        self.assertEqual(Polynomial([2, 4, 0]), Polynomial([1, 2, -4]) + Polynomial([1, 2, 4]))

    def test_add_with_polynomial2(self):
        self.assertEqual(Polynomial([4, 0]), Polynomial([1, 2, -4]) + Polynomial([-1, 2, 4]))

    def test_add_with_polynomial3(self):
        self.assertEqual(Polynomial([1, 1, -2, 14]), Polynomial([1, 2, -4, 10]) + Polynomial([-1, 2, 4]))

    # SUB TESTS

    def test_sub_with_number(self):
        self.assertEqual(Polynomial([1, 2, -5]), Polynomial([1, 2, -4]) - 1)

    def test_sub_with_number2(self):
        self.assertEqual(Polynomial([-1, -2, 7]), 3 - Polynomial([1, 2, -4]))

    def test_sub_with_zero(self):
        self.assertEqual(Polynomial([1, 2, -4]), Polynomial([1, 2, -4]) - 0)

    def test_sub_fail_incorrect_type(self):
        with self.assertRaises(TypeError):
            'test' - Polynomial([1, 2, -4])

    def test_sub_fail_incorrect_type2(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, -4]) - '31'

    def test_sub_with_polynomial(self):
        self.assertEqual(Polynomial([0]), Polynomial([1, 2, -4]) - Polynomial([1, 2, -4]))

    def test_sub_with_polynomial2(self):
        self.assertEqual(Polynomial([2, 0, -8]), Polynomial([1, 2, -4]) - Polynomial([-1, 2, 4]))

    def test_sub_with_polynomial3(self):
        self.assertEqual(Polynomial([1, 3, -6, 6]), Polynomial([1, 2, -4, 10]) - Polynomial([-1, 2, 4]))

    # MUL TESTS

    def test_mul_with_number(self):
        self.assertEqual(Polynomial([3, 6, -12]), Polynomial([1, 2, -4]) * 3)

    def test_mul_with_polynomial(self):
        self.assertEqual(Polynomial([2, 4, -8]), Polynomial([1, 2, -4]) * Polynomial([2]))

    def test_mul_with_polynomial2(self):
        self.assertEqual(Polynomial([1, 4, 0, -8]), Polynomial([1, 2, -4]) * Polynomial([1, 2]))

    def test_mul_with_zero(self):
        self.assertEqual(Polynomial([0]), Polynomial([1, 2, -4]) * 0)

    def test_mul_fail_incorrect_type(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, -4]) * 'test'


    def test_expression(self):
        self.assertEqual(Polynomial([-1, 7, 4, -14]),
                         -(Polynomial([1, -4]) * Polynomial([1, -2, -4])) + Polynomial([1, 8, 2]))

    # EQ TESTS
    def test_eq_polynomials(self):
        self.assertTrue(Polynomial([1, 4, 0, -8]) == Polynomial([1, 4, 0, -8]))

    def test_eq_polynomials_with_zeros(self):
        self.assertTrue(Polynomial([0, 1, 4, 0, -8]) == Polynomial([1, 4, 0, -8]))

    def test_not_eq_polynomials(self):
        self.assertFalse(Polynomial([1, 4, 0, -1]) == Polynomial([1, 4, 0, -8]))

    def test_eq_fail_incorrect_type(self):
        with self.assertRaises(TypeError):
            Polynomial([0, 1, 4, 0, -8]) == 'test'


    # REPR TESTS

    def test_repr(self):
        self.assertEqual('Polynomial([1, 2, -4])', repr(Polynomial([1, 2, -4])))

    def test_repr_with_zeros(self):
        self.assertEqual('Polynomial([1, 2, -4])', repr(Polynomial([0, 1, 2, -4])))

    # STR TESTS

    def test_str(self):
        self.assertEqual('x^2 + 2x - 4',  str(Polynomial([1, 2, -4])))

    def test_str_with_zeros(self):
        self.assertEqual('x^2 + 2x - 4', str(Polynomial([0, 0, 1, 2, -4])))

    def test_str_2_elements(self):
        self.assertEqual('2x - 4', str(Polynomial([2, -4])))

    def test_str_2_first_negative(self):
        self.assertEqual('-2x - 4', str(Polynomial([-2, -4])))

    def test_str_with_middle_zero(self):
        self.assertEqual('5x^2 - 4', str(Polynomial([5, 0, -4])))


if __name__ == '__main__':
    unittest.main()
