# coding:utf-8
import nltk
from nltk.corpus import nps_chat

emma = nltk.corpus.gutenberg.words('austen-emma.txt')

word_count = dict()
word2_count = dict()
prev_word = '#'
word_count['#'] = 1
stops = set(",.[]{}();:'\"?-!#")
for w in emma:
	w = w.lower()
	if w[0] in stops:
		prev_word = '#'
		word_count['#'] += 1
		continue
		
	if w not in word_count:
		word_count[w] = 0
	word_count[w] += 1
	
	word2 = (prev_word, w)
	if word2 not in word2_count:
		word2_count[word2] = 0
	word2_count[word2] += 1
	prev_word = w 
	
word_count_sparse = {w:word_count[w] for w in word_count if word_count[w]>10}
word2_count_sparse = {w:word2_count[w] for w in word2_count if word2_count[w]>10}

for w,c in sorted(word_count_sparse.iteritems(), key=lambda d:d[1], reverse=True):
	print '%s\t%d' % (w, c)
	
print '-------------------------'

sw2cs = sorted(word2_count_sparse.iteritems(), key=lambda d:d[1], reverse=True)
for w,c in sw2cs:
	print '%s %s\t%d' % (w[0],w[1], c)

print '-------------------------'
word_2gram_p = dict()
for ws,c in sw2cs:
	w0 = ws[0]
	w1 = ws[1]
	c0 = 0
	if w0 in word_count_sparse:
		c0 = word_count_sparse[w0]
	word_2gram_p[(w0,w1)]=1.0*c/(1+c0)
	
for ws, p in sorted(word_2gram_p.iteritems(), key=lambda d:d[1], reverse=True):
	print '%s | %s\t%f' % (ws[1],ws[0], p)