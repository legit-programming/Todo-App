import sys, os, json, types, unittest

for i in ["/task", "/workspace", "/program"]:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + i)

import taskManager as TM, workspaceManager as WM, programManager as PM

commands = WM.commands + TM.commands + PM.commands

class Commands(unittest.TestCase):
    def test_commandAttributes(self):
        for i in commands:
            self.assertIn("name", i, "No command name")
            self.assertIn("description", i, "No command description")
            self.assertIn("alias", i, "No command alias")
            self.assertIn("help", i, "No command help")
            self.assertIn("function", i, "No command function")
            self.assertIn("source", i, "No command function")
    
    def test_commandFunctions(self):
        for i in commands:
            self.assertTrue(callable(i["function"]), "Function not callable")
            self.assertTrue(callable(i["source"]), "Source not callable")

    def test_duplicateNames(self):
        self.assertEqual(sum(1 for i in commands for j in commands if i["name"] == j["name"]), len(commands), "Duplicate command name found")

    def test_duplicateAliases(self):
        for i in commands:
            for j in commands:
                if i["name"] != j["name"]:
                    for k in i["alias"]:
                        self.assertNotIn(k, j["alias"], "Duplicate command alias found")

class Data(unittest.TestCase):
    def test_emptyData(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + "/todo.json") as file:
            data = json.load(file, object_hook=lambda d: types.SimpleNamespace(**d))
            self.assertTrue(isinstance(data, list), "Data is not a list")
            self.assertEqual(len(data), 0, "Data must be removed from the list")

if __name__ == '__main__':
    unittest.main(verbosity=2)