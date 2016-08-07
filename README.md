# spam_proj
Spam detection project inspired by an assignment in [Coursera's ML course](https://www.coursera.org/learn/machine-learning).

[Simple website](https://arcane-thicket-31145.herokuapp.com/) that indicates whether an email's contents suggest that the email is spam/not spam.

### Known bugs
1. The vocab.txt file (taken from the Coursera assignment) is not suited for the nltk Porter Stemmer I used. This seems to be the root of misclassification of emailSample1.txt as spam, rather than ham.
