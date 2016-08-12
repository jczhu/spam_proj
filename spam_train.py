import numpy as np
import scipy.io as sio
from sklearn.svm import SVC, LinearSVC

from process_email import get_vocab_list, process_email, email_features

# Trains svm
# email_features should be 2d array, classification is simple list
# training specifies which sklearn package to use
def spam_train(email_features, classification, training):
	X = np.array(email_features)
	y = np.array(classification)

	if training == "svc":
		model = SVC(kernel="linear", probability=True)
	else:
		model = LinearSVC(loss="hinge")

	model.fit(X, y)

	# accuracy on training data, probs not best practice
	print model.score(X, y)

	# accuracy on test data, better practice lel
	# this score is lower than the pdf predicted....hmmm
	test_mat = sio.loadmat('newTest.mat')
	Xtest = test_mat['Xtest']
	ytest = np.ravel(test_mat['ytest'])
	print model.score(Xtest, ytest)

	return model

# Returns 15 words most common (indicative?) of spam
# Can only use if linear svm model
def top_spam_indicators(model):
	coef = np.array(np.ravel(model.coef_))
	return np.argpartition(coef, -15)[-15:]


# for testing
if __name__ == "__main__":
    import sys
    mat_contents = sio.loadmat('newTrain.mat')
    X = mat_contents['X']
    y = np.ravel(mat_contents['y'])
    model = spam_train(X, y, "linear")


    with open("spamSample1.txt", 'r') as myfile: 
		email_contents = myfile.read().replace('\n', '')
    features = np.reshape(email_features(process_email(email_contents)), (1, -1))
    print "Prediction"
    print np.asscalar(model.predict(features))


    print "Top spam indicators"
    tsi = top_spam_indicators(model)
    vocab_list = get_vocab_list("newvocab.txt")
    print [(vocab_list[x]) for x in tsi] # also getting different results here
