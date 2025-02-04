from nltk import PorterStemmer
from nltk.corpus import stopwords
from operator import itemgetter
from random import shuffle
import string
import os
import re
import scipy.io

from process_email import process_email, email_features

def process_lingspam():
	all_paths = ['/part1/', '/part2/', '/part3/', '/part4/', '/part5/', '/part6/', 
	'/part7/', '/part8/', '/part9/', '/part10/']

	# will hold all the processed emails
	all_processed = []

	# binary list that indicates whether corresponding email is spam or not
	# 1 is spam, 0 is ham
	is_spam = []

	for path in all_paths:
		with cd(os.getcwd() + path):
			all_processed, is_spam = process_folder(all_processed, is_spam)

	# remove the first empty element and return
	return all_processed[1:], is_spam[1:]

# remove subject line headers from each file and process the body of the email
# return all the processed results from current folder
# email_list is the list to add processed emails to
# is_spam indicates whether the corresponding email is spam or ham
def process_folder(email_list, is_spam):
	pattern = re.compile(r"spmsg(.*)txt")
	for filename in os.listdir(os.getcwd()):
		with open(filename, 'r') as myfile:
			email_contents = myfile.read().splitlines(True)
			email_list.append(process_email(' '.join(email_contents[2:])))

			# check if spam
			if pattern.match(filename):
				is_spam.append(1)
			else:
				is_spam.append(0)
	
	return email_list, is_spam

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
	word_list = sorted(word_list, key=itemgetter(1), reverse=True)

	# return top 700 words
	return [x for x,_ in word_list[:700]]

# converts all emails into email features to use as training and testing data
def convert_to_features(processed_emails):
	features = []
	for i in range(0, len(processed_emails)):
		features.append(email_features(processed_emails[i]))

	return features

# writes data to mat files (split into training data and testing data)
# shuffles the data in hopes of better results
def write_to_mat(email_features, is_spam):
	index_shuf = range(len(email_features))
	shuffle(index_shuf)
	email_features_shuf = [email_features[i] for i in index_shuf]
	is_spam_shuf = [is_spam[i] for i in index_shuf]

	scipy.io.savemat('stopTrain.mat', 
		mdict={'X': email_features_shuf[:2610], 'y': is_spam_shuf[:2610]})
	scipy.io.savemat('stopTest.mat', 
		mdict={'Xtest': email_features_shuf[2610:], 'ytest': is_spam_shuf[2610:]})

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
# write top words to file called vocab
if __name__ == "__main__": 
	# clean emails for each folder in lingspam
	path = "~/Downloads/lingspam_public/bare/" 
	with cd(path):
		all_processed, spam_list = process_lingspam()
	print len(all_processed)
	# print spam_list
	print len(spam_list)
	vocab = common_words(all_processed)
	# write most common words into vocab
	with open("stopvocab.txt", "w") as myfile:
		for item in vocab:
			myfile.write("%s\n" % item)
	features = convert_to_features(all_processed)
	print len(features)
	print len(features[0])
	write_to_mat(features, spam_list)


