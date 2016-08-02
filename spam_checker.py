import web
import os
import numpy as np
import scipy.io as sio
from sklearn.svm import SVC

from web.contrib.template import render_jinja
from process_email import process_email, email_features
from spam_train import spam_train

template_dir = os.path.join(os.path.dirname(__file__), '.')
render = render_jinja(
    template_dir,
    encoding='utf-8',
)

model = None # store model so won't have to compute over and over

class index:
    def GET(self):
        return render.front(email="", error="")

    def POST(self):
        global model
        email = web.input().email

        if not email:
            error = "we need some email contents"
            return render.front(email=email, error=error)
        else:
            features = email_features(process_email(email))

            # TO DO: add separate method to read in training data
            # TO DO: get training data from elsewhere
            # TO DO: improve model??? Cross-validation somehow?
            if not model:
                mat_contents = sio.loadmat('spamTrain.mat')
                X = mat_contents['X']
                y = np.ravel(mat_contents['y'])
                model = spam_train(X, y)

            if np.asscalar(model.predict(X)) == 1: # predict not single value?
                error = "spam"
            else:
                error = "not spam"
            return render.front(email=email, error=error)
        

urls = (
    '/', 'index'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()



