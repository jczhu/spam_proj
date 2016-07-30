import webapp2
import cgi

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
        email = self.request.get("email")

        if email:
            # do processing stuffs
        else:
            error = "we need some email contents"
            self.render_front(title, email, error)


def escape_html(s):
    return cgi.escape(s, quote = True)


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)