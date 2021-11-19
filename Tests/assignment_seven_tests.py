import unittest
import assignment_seven


class MyTestCase(unittest.TestCase):
    def test_encode_one(self):
        self.assertEqual("sbwkrq", assignment_seven.coding(["python", 3, 'y']))
        self.assertEqual("something", assignment_seven.coding(["xtrjymnsl", -5, 'n']))
        self.assertEqual("xtrjymnsl", assignment_seven.coding(["something", 5, 'y']))
    def test_encode_two(self):
        self.assertEqual("wcescjdpek", assignment_seven.encode("hello world", "python"))

    def test_option_three(self):
        pass



if __name__ == '__main__':
    unittest.main()
