import webapp2
import cgi
import os
import jinja2
import numpy as np
import scipy.io as sio
from sklearn.svm import SVC

from process_email import process_email, email_features
from spam_train import spam_train

template_dir = os.path.join(os.path.dirname(__file__), '.')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

model = None # store model so won't have to computer over and over

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def render_front(self, email="", error=""):
        self.render("front.html", email=email, error=error)

    def get(self):
        return self.render_front()

    def post(self):
        global model
        email = self.request.get("email")

        if email:
            features = email_features(process_email(email))

            # TO DO: add separate method to read in training data
            # TO DO: get training data from elsewhere
            # TO DO: improve model??? Cross-validation somehow?
            if not model:
                mat_contents = sio.loadmat('spamTrain.mat')
                X = mat_contents['X']
                y = np.ravel(mat_contents['y'])
                model = spam_train(X, y)

            if model.predict(X) == 1:
                error = "spam"
            else:
                error = "not spam"
            self.render_front(email, error)
        else:
            error = "we need some email contents"
            self.render_front(email, error)


def escape_html(s):
    return cgi.escape(s, quote = True)


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)