import unittest
from importlib import import_module
module = import_module('tabulator.table')


class TableTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(module.Table)
