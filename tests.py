#!/usr/bin/python3
from task import Task
from phabtree import parse

import unittest

class TestParser(unittest.TestCase):
    def test_basic(self):
        source = """
# {T1337} Header task description
## Subtask 1
### Subtask 1.1
## Subtask 2
### Subtask 2.1
### Subtask 2.2
## Subtask 3
"""
        ref = Task('T1337', 'Header task description')
        ref.subtasks.append(Task(None, 'Subtask 1'))
        ref.subtasks[-1].subtasks.append(Task(None, 'Subtask 1.1'))
        ref.subtasks.append(Task(None, 'Subtask 2'))
        ref.subtasks[-1].subtasks.append(Task(None, 'Subtask 2.1'))
        ref.subtasks[-1].subtasks.append(Task(None, 'Subtask 2.2'))
        ref.subtasks.append(Task(None, 'Subtask 3'))

        self.assertEqual(ref, parse(source))

if __name__ == '__main__':
    unittest.main()
