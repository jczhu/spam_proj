# spam_proj
Spam detection project inspired by an assignment in [Coursera's ML course](https://www.coursera.org/learn/machine-learning).

[Simple website](https://arcane-thicket-31145.herokuapp.com/) that indicates whether an email's contents suggest that the email is spam/not spam.

##Results from cross-validation 
### Removing stopwords from email
- Accuracy on training data: 1.0
- Accuracy on test data: 0.986301369863
- precision on test data: 0.943396226415
- recall on test data: 0.980392156863
- f1 score on test data: 0.961538461538
- Prediction for spamSample2.txt (1 is spam, 0 is not spam): 1
- Top spam indicators: ['us', 'friend', 'compani', 'com', 'index', 'live', 'cd', 'internet', 'phone', 'person', 'number', 'http', 'free', 'dollar', 'click']

### Including stopwords in email
- Accuracy on training data: 1.0
- Accuracy on test data: 0.993150684932
- precision on test data: 0.978260869565
- recall on test data: 0.978260869565
- f1 score on test data: 0.978260869565
- Prediction for spamSample2.txt (1 is spam, 0 is not spam): 0
- Top spam indicators: ['over', 'instruct', 'question', 'cross', 'ani', 'reason', 'found', 'k', 'univers', 'n', 'take', 'again', 'write', 'and', 'deadlin']

#### Decision: removing stopwords.
Although I lose some accuracy and precision, removing stopwords seems to be better. First of all, the top spam indicators are more "spammy" when removing stopwords vs including stopwords. Second, I prefer more recall rather than more precision. But this is more subjective. I prefer recall because I prefer the spam classifier incorrectly classify ham as spam, rather than letting spam slip through as ham. Finally, (this is really minor) the model including stopwords misclassifies spamSample2.txt, which is a very obvious example of spam.

(Note to future self in case I forget)
- Precision in this case is how many of the predicted spam emails are actually spam.
- Recall in this case is how many of the actual spam emails were predicted to be spam.


### Outside sources:
1. [Ling-Spam dataset](http://csmining.org/index.php/ling-spam-datasets.html) used to update my vocab file and used as new training/testing data.
2. Stopwords file (named just "english" in this repository) from [NLTK's](http://www.nltk.org/) stopwords corpus. Directly copied from my local installation of the corpus due to issues with Heroku.
