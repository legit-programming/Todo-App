from types import SimpleNamespace
import json, os, sys, unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/task')
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/workspace')

import taskManager, workspaceManager

commands = workspaceManager.commands + taskManager.commands

class Commands(unittest.TestCase):
    def test_commandAttributes(self):
        for i in commands:
            self.assertIn("name", i)
            self.assertIn("description", i)
            self.assertIn("alias", i)
            self.assertIn("help", i)
            self.assertIn("function", i)
            self.assertIn("source", i)

    def test_duplicateNames(self):
        self.assertEqual(sum(1 for i in commands for j in commands if i["name"] == j["name"]), len(commands))

class Data(unittest.TestCase):
    def test_emptyData(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + "/todo.json") as file:
            data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
            self.assertTrue(isinstance(data, list))
            self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()