from nltk import PorterStemmer
from nltk.corpus import stopwords
from operator import itemgetter
import re
import string
import os

from process_email import process_email, email_features

def process_lingspam():
	all_paths = ['/part1/', '/part2/', '/part3/', '/part4/', '/part5/', '/part6/', 
	'/part7/', '/part8/', '/part9/', '/part10/']

	# will hold all the processed emails
	all_processed = []

	for path in all_paths:
		with cd(os.getcwd() + path):
			all_processed = process_folder(all_processed)

	# remove the first empty element and return
	return all_processed[1:]

# remove subject line headers from each file and process the body of the email
# return all the processed results from current folder
# email_list is the list to add processed emails to
def process_folder(email_list):
	for filename in os.listdir(os.getcwd()):
		with open(filename, 'r') as myfile:
			email_contents = myfile.read().splitlines(True)
			email_list.append(process_email(' '.join(email_contents[2:])))
	
	return email_list

# finds most common words in processed emails
# processed_emails is the list of lists of processed emails
def common_words(processed_emails):
	# create dictionary of all the word stems in the processed emails
	word_dict = {}
	for i in range(0, len(processed_emails)):
		for word in processed_emails[i]:
			if not word in word_dict:
				word_dict[word] = 1
			else:
				word_dict[word] += 1

	# sort the words in order of frequency (most frequent to least)
	word_list = word_dict.items()
	word_list = sorted(word_list, key=itemgetter(1))

	# return first 2000 tuples
	return word_list[:2000]

class cd:
    """Context manager for changing the current working directory"""
    # obtained from Brian Hunt's answer to a Stack Overflow question at
    # http://stackoverflow.com/questions/431684/how-do-i-cd-in-python/24176022#24176022
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

# for testing, and eventually for parsing all the raw email files
if __name__ == "__main__": 
	# clean emails for each folder in lingspam
	path = "~/Downloads/lingspam_public/bare/" 
	with cd(path):
		all_processed = process_lingspam()
	print len(all_processed)
	print common_words(all_processed)


