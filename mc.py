import os
import sys
import random
import string


trainingData = open('./Data.txt').readlines()

table = {} #lol will get massive

data = []
words = []


for line in trainingData:
	for word in line.split():
		words.append(word)

for idx in xrange(0,len(words)-2):
	w1, w2, w3 = words[idx], words[idx+1], words[idx+2]
	w1 = w1.translate(string.maketrans("",""), string.punctuation)
	w2 = w2.translate(string.maketrans("",""), string.punctuation)
	w3 = w3.translate(string.maketrans("",""), string.punctuation)	
	words[idx], words[idx+1], words[idx+2] = w1, w2, w3
	
	key = (w1,w2)
	val = w3
	
	if key in table:
		table[key].append(val)
	else:
		table[key] = [val]
	

seed = random.randint(0, len(words)-3)
w1, w2 = words[seed], words[seed+1]
gen = []

for i in xrange(0,int(sys.argv[1])):
	gen.append(w1)
	w1, w2 = w2, random.choice(table[(w1,w2)])


print ' '.join(gen)

