# Importing dependencies
import os
from os.path import exists as file_exists
import unittest


class TestInstall(unittest.TestCase):

   #  Tests the correct installation of the cosmic variants

    def cosmic_variants_exist(self):
        cosmic_variants_path = os.path.abspath(
            "cosmic_variants.tsv")
        self.assertEqual(file_exists(cosmic_variants_path), True)

    def correct_output(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
