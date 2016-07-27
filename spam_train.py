import numpy as np
import scipy.io as sio
from sklearn.svm import SVC

#from process_email import email_features, process_email

# Trains svm
# email_features should be 2d array, classification is simple list
def spam_train(email_features, classification):
	X = np.array(email_features)
	y = np.array(classification)

	model = SVC(kernel="linear", probability=True)
	model.fit(X, y)
	SVC(kernel = "linear") # need to read up on them parameters

	# accuracy on training data, probs not best practice
	print model.score(X, y)

	# accuracy on test data, better practice lel
	# this score is lower than the pdf predicted....hmmm
	test_mat = sio.loadmat('spamTest.mat')
	Xtest = test_mat['Xtest']
	ytest = np.ravel(test_mat['ytest'])
	print model.score(Xtest, ytest)

# for testing
if __name__ == "__main__":
    import sys
    mat_contents = sio.loadmat('spamTrain.mat')
    X = mat_contents['X']
    y = np.ravel(mat_contents['y'])
    spam_train(X, y)
