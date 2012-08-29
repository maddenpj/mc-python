import os
import sys
import random
import string


trainingData = open('./Data.txt').readlines()

table = {} #lol will get massive

data = []
words = []

ChainLength = 2
Size = int(sys.argv[1])
if(len(sys.argv) >= 3): ChainLength = int(sys.argv[2])


for line in trainingData:
	for word in line.split():
		word = word.translate(string.maketrans("",""), string.punctuation)
		words.append(word)

for idx in xrange(0,len(words)-ChainLength):
	ws = words[idx:idx+ChainLength+1]
	
	key = tuple(ws[:ChainLength])
	val = ws[ChainLength]
	if key in table:
		table[key].append(val)
	else:
		table[key] = [val]
	

seed = random.randint(0, len(words)-ChainLength+1)
ws = words[seed:seed+ChainLength] 
gen = []

for i in xrange(0,int(sys.argv[1])):
	gen.append(ws[0])
	val = random.choice(table[tuple(ws)])
	ws.append(val)
	ws.pop(0)

print ' '.join(gen)

