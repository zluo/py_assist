"""


"""

from icrawler.builtin import GoogleImageCrawler
import time
from collections import defaultdict
import os


class IClawer:
    word_time = defaultdict(list)
    word_mem = defaultdict(list)
    root_dir = '/home/zluo/dictionary/'

    def __init__(self):
        pass

    def _isDownloaded(self, key):
        return os.path.isdir(self.root_dir + key)

    def claw(self, keyword, size=10):
        if self._isDownloaded(keyword):
            print(keyword, 'has already downloaded')
            return

        start = time.time()

        google_crawler = GoogleImageCrawler(storage={'root_dir': self.root_dir + keyword})
        google_crawler.crawl(keyword=keyword, max_num=size)
        end = time.time()
        print(end - start)

    def read_log(self):
        with open('logs/words.log', 'r') as f:
            line = f.readline()
            while line:
                line = f.readline()
                items = line.split(',')
                if len(items) == 3:
                    word = items[1]
                    self.word_time[word].append(items[0])
                    self.word_mem[word].append(int(items[2]))

    def download(self):
        self.read_log()
        for k, v in self.word_time.items():
            print(k)
            self.claw(k, 10)


clawer = IClawer()
clawer.download()
