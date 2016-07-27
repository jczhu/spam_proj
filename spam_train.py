import numpy as np
from sklearn.svm import SVC

import process_email as pe #?

# Trains svm
# email_features should be 2d array, classification is simple list
def spam_train(email_features, classification):
	X = np.array(email_features)
	y = np.array(classification)

	model = SVC(kernel="linear", probability=True)
	model.fit(X, y)
	SVC(kernel = "linear") # need to read up on them parameters

	#print model.predict([some appropriately long 2d array]) 

# for testing
if __name__ == "__main__":
    import sys
    spam_train(sys.argv[1])