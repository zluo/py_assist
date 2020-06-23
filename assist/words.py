'''
words statistic of my own.
know_words
new_words.log append word and timestamp to words.log
'''

import datetime
import time
from collections import defaultdict
from ecdict.stardict import StarDict
from ecdict.dictutils import Generator
import os
import glob
import nltk
import sys

class Word():
    WORD_LOG_FILE ='logs/words.log'
    DIC_LOG_FILE = 'logs/dictionary.log'
    DIC_WITH_SAMPLE_LOG_FILE= 'logs/dictionary_with_sample.log'
    MY_BOOKS_DIR = '/home/zluo/src/hp/notes/books'
    texts = []

    def __init__(self):
        self.stardict = StarDict(os.getcwd() + '/ecdict/stardict.db')
        self.generator = Generator()
        self.word_time =defaultdict(list)
        self.word_mem = defaultdict(list)
        self.read_log()

    def generate_sample(self,w):
        if not self.texts:
            self._load_books()
        for text in self.texts:
            print (text.concordance(w))

    def read_log(self):
        with open(self.WORD_LOG_FILE, 'r') as f:
            line = f.readline()
            while line:
                line = f.readline()
                items = line.split(',')
                if len(items)==3:
                    word = items[1]
                    self.word_time[word].append(items[0])
                    self.word_mem[word].append(int(items[2]))


    def show_log(self):
        for k,v in self.word_time.items():
            print(k)


    def show_logv(self):
        for k,v in self.word_time.items():
            self._print_word(k)


    def write_dictionary(self):
        i = 1
        with open(self.DIC_LOG_FILE, 'w') as f:
            for k,v in self.word_time.items():
                self._generate_message(f,k ,i)
                i += 1

    def _load_books(self):
        files = self._get_books_filename()
        for file_name in files:
            print(file_name)
            f=open(file_name ,'rU')
            raw=f.read().decode('utf8')
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            self.texts.append(text)

    def write_log(self, word):
        ts = time.time()
        message = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d') + ',' + word + ',0\n'
        with open(self.WORD_LOG_FILE, 'a') as f:
            f.write(message)

    def _get_books_filename(self):
        result = []
        for x in os.walk(self.MY_BOOKS_DIR):
            for y in glob.glob(os.path.join(x[0], '*.txt')):
                result.append(y)
        return result
        


    def _generate_message(self, f, k, i):
        data = self.stardict.query(k)
        if data is None:
            return
        definition = data.get('definition')
        phonetic = data.get('phonetic')
        translation = data.get('translation')
        tag = self.generator.word_tag(data)

        message = '\n' + str(i) + '. ' + k
        if phonetic is not None: 
            message = message + ' [' + phonetic.encode('utf-8') + ']'
        
        if tag is not None:
            tag = tag.encode('utf-8')
            message = message + ' '*(80- len(message) - len(tag)) + tag
        
        f.write(message + '\n')
        f.write('-'*80 + '\n')

        if translation is not None:
            message = translation.encode('utf-8')
            f.write(message +'\n')

        if definition is not None:
            f.write('\n' + definition + '\n')

        f.write('\n')

    def _print_word(self, k):
        print(k)
        print('-'*80)
        data = self.stardict.query(k)
        if data is not None:
            print(data.get('definition'))
            print(data.get('phonetic'))
            print(data.get('transalation'))
            print(self.generator.word_tag(data))
   