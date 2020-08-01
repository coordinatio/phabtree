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
