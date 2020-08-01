#!/usr/bin/python3
from task import Task

import re

def describe(tsk):
    for t in tsk.subtasks:
        describe(t)
    print(tsk)


def parse(strings):
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
