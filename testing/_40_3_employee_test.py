import os

os.chdir("D:/Python/testing")
import unittest
from _40_4_employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Storm", 60000)

    def tearDown(self):
        print("tearDown", end="\n")

    def test_email(self):

        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Storm@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Storm@email.com")

    def test_fullname(self):

        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Storm")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Storm")

    def test_apply_raise(self):

        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 50000 * 1.04)
        self.assertEqual(self.emp_2.pay, 60000 * 1.04)


if __name__ == "__main__":
    unittest.main()
