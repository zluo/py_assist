import nltk
from nltk.book import *
import operator
import sys
print '----------------', sys.argv[1:]

file_name = 'the_old_man_and_the_sea.txt'

if (len(sys.argv) > 1):
  file_name = sys.argv[1]

'''
  Open file
'''
f=open(file_name ,'rU')

raw=f.read().decode('utf8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)


def lexical_diversity(text):
    return 100.0 * len(set(text))/len(text)

'''
  Write words to files

'''

words = sorted(set(map(lambda w: w.lower(), set(text))))
print words

v_file_name = 'v_' + file_name
v_file = open(v_file_name, 'w')

v_file.write("\n".join(words).encode('utf-8').strip())





prepositions = ['about','above','across' ,'after' ,'against','along','among', 'around', 'as', 'at', 'before', 'behind', 'below', 'beside', 'beneath', 'between', 'beyond', 'by', 'despite', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'opposite', 'out', 'outside', 'over', 'past', 'round', 'since', 'than', 'through', 'to', 'towards','under','underneath','unlike', 'until', 'up', 'upon', 'via', 'with', 'within', 'without']


fdist1 = FreqDist(text)

pf = {key: fdist1[key] for key in prepositions}

pf1 = sorted(pf.items(), key=operator.itemgetter(1))
print '--------------------------------------------------------------------------------'

print 'Q: How many words are there in the text?'
print 'A: ' , len(text)
print ''

print 'Q: How many vocabulary are there ?'
print 'A: ' , len(set(text))
print ''

print 'Q: Lexical Diversity?'
print 'A: ' , lexical_diversity(text)

print pf1



print '------------------------------Done-----------------------------------------------'
