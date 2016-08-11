from nltk import PorterStemmer
from nltk.corpus import stopwords
import re
import string

# Reads in vocab list from filename and convert to python list.
# Assumes vocab list file separates vocab by new line. May have to change.
def get_vocab_list(filename):
    vocab = []
    f = open(filename, 'r')
    for line in f:
    	line = line.strip("0123456789 \n\t") # removes num due to vocab.txt format
        vocab.append(line)
    f.close()
    return vocab

# Processes email by modifying urls, trimming words to word roots, removing punctuation.
# Returns list of word indices
def process_email(email_contents):
	little_words = stopwords.words("english")

	email_contents = email_contents.lower() 	# hopefully not redundant

	# strip all html, using Coursera's regex (may have to change)
	email_contents = re.sub(r"<[^<>]+>", " ", email_contents)

	# replace all numbers with string "number"
	email_contents = re.sub(r"[0-9]+", "number", email_contents)

	# handle urls
	email_contents = re.sub(r"(http|https)://[\S]*", "httpaddr", email_contents)

	# handle email addresses
	# Original Coursera just looks for @, so I amped it up a bit by looking for period
	email_contents = re.sub(r"[\S]+@[\S]+\.[\S]+", "emailaddr", email_contents)

	# handle dollar sign
	email_contents = re.sub(r"[$]+", "dollar", email_contents)

	# after doing all that, strip punctuation
	email_contents = re.sub(r"[^a-zA-Z0-9]", " ", email_contents)

	# remove stop words
	email_contents = ' '.join([word for word in email_contents.split() 
		if word not in little_words])

	# Tokenize email and convert individual words to numbers, based on vocab list
	tokens = email_contents.split()
	for i in range(0, len(tokens)):
		tokens[i] = PorterStemmer().stem_word(tokens[i])

	return tokens

# Email features. Converting list of tokens post processing to logical list.
# The list has 1s in the indices when that word is present in the processed email
def email_features(word_indices):
	vocab_list = get_vocab_list("vocab.txt") # should probably store length to save time
	email_features = [0] * len(vocab_list)

	# could also do for token in word_indices, but vocab_list length is less variable
	for i in range(0, len(vocab_list)):	
		if vocab_list[i] in word_indices:
			email_features[i] = 1

	#for testing, print how many non-zero elements there were 
	# print sum(email_features)

	return email_features

# for testing
if __name__ == "__main__":
   import sys
   with open(sys.argv[1], 'r') as myfile: 
   	email_contents = myfile.read().replace('\n', ' ')
   email_features(process_email(email_contents))
