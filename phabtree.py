#!/usr/bin/python3
import re
import unittest
import pdb

class Task:
    def __init__(self, tid, header):
        self.tid = tid
        self.header = header
        self.subtasks = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "%s %s %s" % (self.tid, self.header, self.subtasks)

    def __eq__(self, other):
        return self.tid == other.tid\
                and self.header == other.header\
                and self.subtasks == other.subtasks


def describe(tsk):
    for t in tsk.subtasks:
        describe(t)
    print(tsk)


def parse(strings):
#    pdb.set_trace()
    parents = []
    for line in strings.splitlines():
        m = re.search(r'^(#+)\s*(?:{(T\d+)})?\s*(.*)$', line)
        if not m:
            continue
        lvl = len(m.group(1))
        tsk = Task(m.group(2), m.group(3))
        if not parents:
            parents.append(tsk)
        elif lvl > len(parents):
            parents[-1].subtasks.append(tsk)
            parents.append(tsk)
        else:
            parents = parents[:lvl-1]
            parents[-1].subtasks.append(tsk)
            parents.append(tsk)
    return parents[0]



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
