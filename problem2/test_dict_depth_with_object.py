import sys
import unittest
from io import StringIO
from unittest import TestCase

from problem2.dict_depth_with_object import Person, print_depth


class Test(TestCase):
    def test_print_depth(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b
                }
            }
        }
        print_depth(a)

        sys.stdout = sys.__stdout__
        expected = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n" \
                   "user 3\nfirst_name 4\nlast_name 4\nfather 4\n" \
                   "first_name 5\nlast_name 5\nfather 5\n"
        print('output:', captured_output.getvalue())
        print('expected:', expected)
        self.assertEqual(captured_output.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()