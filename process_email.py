from nltk import PorterStemmer
import re

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
def process_email(email_file):
	vocab_list = get_vocab_list("vocab.txt")

	with open(email_file, 'r') as myfile:
		email_contents = myfile.read().replace('\n', '')

	email_contents = email_contents.lower() 	# hopefully not redundant

	# strip all html, using Coursera's regex (may have to change)
	email_contents = re.sub(r"<[^<>]+>", " ", email_contents)

	# replace all numbers with string "number"
	email_contents = re.sub(r"[0-9]+", "number", email_contents)

	# handle urls
	email_contents = re.sub(r"(http|https)://[^\S]*", "httpaddr", email_contents)

	# handle email addresses
	# Original Coursera just looks for @, so I amped it up a bit by looking for period
	email_contents = re.sub(r"[\S]+@[\S]+\.[\S]+", "emailaddr", email_contents)

	# handle dollar sign
	email_contents = re.sub(r"[$]+", "dollar", email_contents)

	# after doing all that, remove all non alphanumeric characters
	email_contents = re.sub(r"[^a-zA-Z0-9]", " ", email_contents)

	# Tokenize email and convert individual words to numbers, based on vocab list
	tokens = email_contents.split()
	for i in range(0, len(tokens)):
		tokens[i] = PorterStemmer().stem_word(tokens[i])
		try:
			temp = vocab_list.index(tokens[i])
		except ValueError:
			tokens[i] = ""
		else:
			tokens[i] = temp

	# Concatenate elements into a string
	processed = ' '.join(map(str, tokens))

	# Print out string. For testing purposes.
	print processed

# for testing
if __name__ == "__main__":
    import sys
    process_email(sys.argv[1])
