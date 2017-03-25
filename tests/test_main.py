import unittest

from create_box import create_box, create_box1

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = '''
****
*  *
****
'''.lstrip()

class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    def test_new_box(self):
        self.assertEqual(create_box(3,24,'x'), third_box_expected)

    def test_box2(self):
        self.assertEqual(create_box1(3,4,'*'), fourth_box_expected)

"""
https://www.tutorialspoint.com/python/string_lstrip.htm
https://www.tutorialspoint.com/python/string_rstrip.htm
"""
