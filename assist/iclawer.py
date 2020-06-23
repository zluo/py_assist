"""

"""

from icrawler.builtin import GoogleImageCrawler
import time
class IClawer:

    def __init__(self):
        pass

    def claw(self, keyword, size=10):
        start =time.time()

        google_crawler = GoogleImageCrawler(storage={'root_dir': '/home/zluo/food/' + keyword})
        google_crawler.crawl(keyword=keyword + ' dishes', max_num=size)
        end = time.time()
        print(end - start)






keydict = {'healthy': {'scallop'}}

keywords={'burger', 'seafood', 'salard', 'egg', 'fish', 'meat', 'veg', 'fruit', 'fast food', 'coconut', 'mushroom', 'pizza', 'soup','cheese','stew',
              'beef','lamb', 'sausage', 'seasame seed', 'pork', 'shrimp', 'bread', 'breakfast', 'dumpling', 'noddle','bread','potato','rice', 'maize', 'Sushi','chicken',
              'duck','ham', 'sandwich', 'turkey','pineapple', 'grape','pasta','goose', 'pudding', 'chunky', 'bean', 'rib','barbecue','eggplant','tomato','seaweed', 'tofu',
          'wraps','pepper','onion','micheline starred', 'meatball','pickled', 'omelette','pancake','bacon','spaghetti','carrot','pumpkin','celery','cucumber', 'cabbage','cauliflower','keto','vegan', 'curry','restaurant','moule', 'fries'}


seafoods={'crab', 'crab cake', 'thai crab', 'lobster', 'fish egg','scallop', 'squid', 'oyster', 'salmon', 'tuna'}
vegs={}
fruits={'mango', 'mango tenderloin','avocado', 'avocado pasta', 'avocado omelette','stawberry', 'banana'}
meats={}

main={'rice', 'noodle', 'pancake'}

rice_dishes={'paella', 'filipino', 'rice egg', 'arroz', 'rice seafood', 'con leche', 'rice pudding', 'rice soup', 'vietnamese pho soup'}
soups = {'chicken soup', 'french soup', 'burger soup', 'vegetable soup', 'healthy soup', 'chunky soup', 'fish soup', 'filipino soup', 'bean soup', 'carrot soup','cabbage soup','irish potatoes','mashed potatos', 'beef stew'}
porks = {'pork stuffed', 'lettuce wraps', 'pulled pork', 'healthy pulled pork', 'pork tenderloin', 'lamb tenderloin', 'beef tenderloin'}

cookmethods ={'boiled', 'steam', 'fried', 'stew', 'roast','bbq', 'smoked','stir fry', 'soup', 'pickled'}
nationals ={'french','italian', 'indian', 'chinese', 'greek' ,'mexico', 'japanese','korean','sichuan','arabian', 'brazil','guangdong', 'spanish','russian', 'german', 'thai', 'irish', 'jamaican','cuba','british','scottish', 'sweden','singapore','vietnamese'}
clawer = IClawer()
#for keyword in ks:
#    clawer.claw(keyword)
clawer.claw('vietnamese pho soup', 1000)
