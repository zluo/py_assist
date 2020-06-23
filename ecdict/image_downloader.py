"""

"""

from icrawler.builtin import GoogleImageCrawler
import time
class IClawer:

    def __init__(self):
        pass

    def claw(self, keyword, size=10):
        start =time.time()

        google_crawler = GoogleImageCrawler(storage={'root_dir': '/home/zluo/dictionary/' + keyword})
        google_crawler.crawl(keyword=keyword, max_num=size)
        end = time.time()
        print(end - start)

