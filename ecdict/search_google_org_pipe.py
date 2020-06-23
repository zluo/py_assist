
import glob
from PIL import Image
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
import socket
from stardict import StarDict
from stardict import stripword
from dictutils import Generator
from image_downloader import IClawer
import os
import sys
sys.path.insert(0, os.getcwd())
from assist.words import Word

class SearchEngine:
    GOOGLE_SEARCH_QUERY = "http://www.google.com/search?q="
    def __init__(self):
        self._driver = None
        self._generator = Generator()
        # Create Dictionary object with Sqlite database file
        self._stardict = StarDict(os.getcwd() + '/ecdict/stardict.db')
        self._word = Word()

    # read_from_pipe.py
    def _pipe_input(self):
        with open("/home/zluo/pipes/my_pipe", "r", 0) as f:
            word = f.readline()
            f.close()
        return stripword(word)

    def start(self):
        while True:
            word = self._pipe_input()
            self._word.write_log(word)

            # word = raw_input("Enter Word:")
            if word == 'q':
                break
            print(word, '-' * 80)
            data = self._stardict.query(word)
            if data:
                print(data.get('phonetic'), data.get('definition'), data.get('translation'))
                print(self._generator.word_tag(data))
#                self.show_image(word)
            try:
                if self._driver is None:
                    self._driver = webdriver.Firefox()
                    
                self._driver.get(self.GOOGLE_SEARCH_QUERY + word + "&tbm=isch")
            except WebDriverException:
                self._driver = webdriver.Firefox()
                try:
                    self._driver.get(self.GOOGLE_SEARCH_QUERY + word + "&tbm=isch")
                except WebDriverException:
                    # Do nothing
                    print(WebDriverException)


        if self._driver is not None:
            self._driver.close()
        self._stardict.close()
        print('Search Engine Close ...')

    def show_image(self, word):
        image_list = []
        for filename in glob.glob('/home/zluo/dictionary/' + word + '/*.*'): #assuming gif
            im=Image.open(filename)
            im.show()

searchEngine = SearchEngine()
searchEngine.start()
