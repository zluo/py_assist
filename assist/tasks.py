"""
Simple Task Management Class, supported function includes:

- Add new task
- List tasks with statues
- Update task statue
- Show task history

"""

from assist.utils import *
from collections import defaultdict


class Task:
    LOG_FILE ='logs/tasks.log'

    tasks = defaultdict(list)
    status = set(['new', 'close', 'start', 'block', 'reopen', 'history', 'progress'])

    def __init__(self):
        self._load_task()
        # print self.tasks
        pass

    def dispatch(self, args):
        """
        dispatch task actions according to command line input
        """
        # No arguments, show new tasks
        if len(args) == 0:
            self.list_task(['new'])
            return

        items = [i for i in args.split(' ') if len(i) > 0]

        # Arguments are status keyword, show tasks with specified status
        if set(items).issubset(self.status):
            if 'history' in items:
                self.show_all_history()
            else:
                self.list_task(items)
            return

        # first argument is integer, second argument is status, update task status
        if len(items) == 2 and (to_int(items[0]) in self.tasks) and (items[1] in self.status):
            if items[1] == 'history':
                self.show_history(to_int(items[0]))
            else:
                self.update_task(to_int(items[0]), items[1])
            return

        # otherwise, add new task
        self.add_task(args)
        pass

    def update_task(self, key, status):
        item = list(self.tasks[key][-1])
        if item[-1] != status:
            item[-1] = status
            item[1] = time_stamp()
            self.tasks[key].append(item)
            self.write_log(key, item)

    def add_task(self, word):
        seq_no = generat_sequence(self.tasks.keys())
        item = [str(seq_no), time_stamp(), word, 'new']
        self.write_log(seq_no, item)

    def write_log(self, key, item):
        self.tasks[key].append(item)
        message = ';'.join(item) + '\n'
        with open(self.LOG_FILE, 'a') as f:
            f.write(message)

    def _load_task(self):
        with open(self.LOG_FILE, 'r') as f:
            line = f.readline().rstrip('\n')
            while line:
                items = line.split(';')
                # print items
                if len(items) == 4:
                    key = int(items[0])
                    self.tasks[key].append(items)
                line = f.readline().rstrip('\n')
        pass

    def list_task(self, status):
        for key in self.tasks.keys():
            items = self.tasks[key]
            item = items[-1]
            if item[-1] in status:
                message = ' : '.join(item)
                if item[-1] == 'close':
                    message = message + ' (' + str(duration(items[0][1],items[-1][1])) + ')'
                print(message)

    def show_history(self, key):
        items = self.tasks[key]
        for item in items:
            message = ' : '.join(item)
            if item[-1] == 'close':
                message = message + ' (' + str(duration(items[0][1],items[-1][1])) + ')'
            print(message)
        pass

    def show_all_history(self):
        for key in self.tasks.keys():
            if len(self.tasks[key]) > 1:
                self.show_history(key)
                print('-' * 80)

