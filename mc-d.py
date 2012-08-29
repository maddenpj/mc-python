import os
import sys
import random
import string


trainingData = open('./Data.txt').readlines()

# Used for storing the Markov states
table = {} 

# Stores all the words
words = []

# The size of the tuple that represents the Markov State
ChainLength = 2
# Length of hte output chain
Size = int(sys.argv[1])
if(len(sys.argv) >= 3): ChainLength = int(sys.argv[2])

# Read in data and split into words
for line in trainingData:
	for word in line.split():
		#word = word.translate(string.maketrans("",""), string.punctuation)
		words.append(word)
# For each set of words
for idx in xrange(0,len(words)-ChainLength):
	# Now we have ChainLength+1 amount of words
	ws = words[idx:idx+ChainLength+1]
	
	# Construct our table
	# For example Chain Lenght of 2
	# A valid key val pair would be 
    # table[('see', 'spot')] = ['run','play']
    # Indicating that if you are in teh state of ('see', 'spot') the next word has a 50% chance of being run and a 50% chance of being play
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
	# Actually find the next word randomally given the current state Ie: the tuple of words 
	val = random.choice(table[tuple(ws)])
	ws.append(val)
	ws.pop(0)

print ' '.join(gen)

