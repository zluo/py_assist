"""
Write notes from command line. one feature is automatically add date , like a dairy.
notes listed by date.
"""

from assist.utils import *
from collections import defaultdict


class Note:
    NOTES_LOG_FILE = 'logs/notes.log'
    notes = defaultdict(list)

    def __init__(self):
        try:
            self._load_note()
        except Exception as e:
            print(e)
        pass

    def dispatch(self, args):
        """
        dispatch note actions according to command line input
        """
        # No arguments, show new notes
        if len(args) == 0:
            self.show_key(date_stamp())
            return

        # otherwise, add new note
        if args == 'all':
            self.show_all_keys()
            return
        self.add_note(args)
        pass

    def add_note(self, word):
        key = date_stamp()
        if not key in self.notes:
            self.write_log('--------' + key + '---------')

        self.notes[key].append(word)
        self.write_log(word)

    def write_log(self, message):
        with open(self.NOTES_LOG_FILE, 'a') as f:
            f.write(message)
            f.write('\n')

    def _load_note(self):
        key = date_stamp()
        with open(self.NOTES_LOG_FILE, 'r') as f:
            whole_line = f.readline()
            while whole_line:
                line = whole_line.rstrip('\n')
                if line.startswith('-----'):
                    key = line.strip('-')
                else:
                    self.notes[key].append(line)
                whole_line = f.readline()
        pass

    def show_key(self, key):
        print('---------' ,key , '----------')
        messages = self.notes[key]
        for message in messages:
            print(message)
        pass

    def show_all_keys(self):
        for key in self.notes.keys():
            self.show_key(key)
