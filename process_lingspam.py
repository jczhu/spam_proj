from nltk import PorterStemmer
from nltk.corpus import stopwords
import re
import string
import os

from process_email import process_email, email_features

def process_lingspam():
	all_paths = ['/part1/', '/part2/', '/part3/', '/part4/', '/part5/', '/part6/', 
	'/part7/', '/part8/', '/part9/', '/part10/']
	for path in all_paths:
		with cd(os.getcwd() + path):
			process_folder()

# remove subject line headers from each file and process the body of the email
# store the result in a new folder called "cleaned"
def process_folder():
	# make cleaned folder
	print os.getcwd()
	try: 
		os.makedirs(os.getcwd() + "/cleaned")
	except OSError:
		if not os.path.isdir(os.getcwd() + "/cleaned"):
			raise
	print "folder" + os.getcwd()

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
		process_lingspam()




