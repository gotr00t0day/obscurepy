import unittest
from obscurepy.utils.definition_tracker import DefinitionTracker


class TestDefinitionTracker(unittest.TestCase):

    def setUp(self):
        self.fixture = DefinitionTracker.get_instance()
        self.fixture.clear_definitions()
        self.test_class = class_dict = {
            'new_name': "NewClassName",
            'prev_name': "TestClass",
            'variables': [],
            'properties': [],
            'methods': [],
            'bases': []
        }
        self.test_function = class_dict = {
            'new_name': "NewFunctionName",
            'prev_name': "TestFunction",
            'variables': [],
            'args': [],
            'return': 'some_variable'
        }
        self.test_variable = {'name': 'test_variable'}

    def test_singleton(self):
        with self.assertRaises(Exception):
            DefinitionTracker()

    def test_add_class(self):
        self.fixture.add_class(self.test_class)
        self.assertEqual(len(self.fixture.definitions['classes']), 1)

    def test_get_class(self):
        self.fixture.add_class(self.test_class)
        class_ = self.fixture.get_class("TestClass")
        self.assertEqual(class_['new_name'], "_0x397")

    def test_add_function(self):
        self.fixture.add_function(self.test_function)
        self.assertEqual(len(self.fixture.definitions['functions']), 1)

    def test_get_function(self):
        self.fixture.add_function(self.test_function)
        function = self.fixture.get_function("TestFunction")
        self.assertEqual(function['new_name'], "_0x4e7")

    def test_add_variable(self):
        self.fixture.add_variable("TestVariable")
        self.assertEqual(len(self.fixture.definitions['variables']), 1)

    def test_get_variable(self):
        self.fixture.add_variable("TestVariable")
        variable = self.fixture.get_variable("TestVariable")
        self.assertEqual(variable, "_0x4c6")
