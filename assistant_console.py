""" assistant command line shell """
import signal
from cmd import Cmd
import subprocess
from assist.tasks import Task
from ecdict.stardict import StarDict
from ecdict.dictutils import Generator
from assist.notes import Note
from assist.words import Word
import sys
import os


class AssistantConsole(Cmd):
    task = Task()
    note = Note()
    word = Word()
    proc = subprocess.Popen([sys.executable, os.getcwd() + "/ecdict/search_google_org_pipe.py"])
    current_input = ''

    def do_c(self, args):
        """ Clean console output """
        print('\n' * 80)

    def do_n(self, args):
        """write note command"""
        self.note.dispatch(args)

    def do_q(self, args):
        """Quit assistant console"""
        print("Quitting....")
        self.proc.terminate()
        raise SystemExit

    def do_t(self, args):
        """
           Show currrent word samples
        """

    def do_t(self, args):
        """add a new task start or list tasks
           t               show new tasks
           t <num> close   close task
           t <num> reopen  reopen task
           t history       show all history
           t <status>      show tasks in certain status, such as 'new', 'close', 'start', 'block', 'reopen', 'history', 'progress'
        """
        self.task.dispatch(args)

    def do_w(self, args):
        """search new words in dictionary. send the keyword to my_pipe  pipeline
           w l  list all words
           w d  generate dictionary
           w lv list all words in verbose format
           w s generate dictionary with samples
            self.word.show_log()
            return
        """
        if args == 'lv':
            self.word.show_logv();
            return

        if args == 'd':
            self.word.write_dictionary()
            return

        if args == 's':
            self.word.generate_sample(self.current_input)
            return

        if len(args) != 0:
            self.current_input = args
        else:
            args = self.current_input
            print(args)
        subprocess.Popen(["echo " + args + " > /home/zluo/pipes/my_pipe "], shell=True)

    def do_v(self, args):
        """
          Generate vocabulary dictionary
        """
        self.word.generate_word(self.current_input)

    def default(self, args):
        length = sum(len(s) for s in args)
        if length < 30 and self._is_ascii(args):
            self.do_w(args)
        else:
            self.do_n(args)

    def _is_ascii(self, s):
        try:
            s.decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True


if __name__ == '__main__':
    os.setpgrp() # create new process group, become its leader
    try:
        prompt = AssistantConsole()
        prompt.prompt = '> '
        prompt.cmdloop('Type help to list all commands...')
    finally:
        os.killpg(0, signal.SIGKILL) # kill all processes in my group
