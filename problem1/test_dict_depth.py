import sys
import unittest
from io import StringIO

from problem1.dict_depth import print_depth


class TestDictDepth(unittest.TestCase):
    def test_print_depth(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        print_depth(a)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n")


if __name__ == '__main__':
    unittest.main()
