import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk import wordpunct_tokenize          
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import words
from string import punctuation
import numpy as np
from sklearn.utils import shuffle
import nltk
#nltk.download('stopwords')
#nltk.download('words')
#nltk.download('wordnet')

class LemmaTokenizer(object):
    def __init__(self, remove_non_words=True):
        self.wnl = WordNetLemmatizer()
        self.stopwords = set(stopwords.words('english'))
        self.words = set(words.words())
        self.remove_non_words = remove_non_words
    def __call__(self, doc):
        # tokenize words and punctuation
        word_list = wordpunct_tokenize(doc)
        # remove stopwords
        word_list = [word for word in word_list if word not in self.stopwords]
        # remove non words
        if(self.remove_non_words):
            word_list = [word for word in word_list if word in self.words]
        # remove 1-character words
        word_list = [word for word in word_list if len(word)>1]
        # remove non alpha
        word_list = [word for word in word_list if word.isalpha()]
        return [self.wnl.lemmatize(t) for t in word_list]

class spam_data_loader:
    def __init__(self): 
        self.train_dir = ''
        self.email_path = []
        self.email_label = []
        self.countvect = CountVectorizer(input='filename',tokenizer=LemmaTokenizer(remove_non_words=True))
        self.word_count = None
        self.feat2word = None
        self.tfidf_transformer = TfidfTransformer()
        self.tfidf = []
    def load_data(self,email_path=None,verbose=False):
        # Define email path
        if(email_path==None):
            self.train_dir = '../data/lingspam_public/bare/'
            self.email_path = []
            self.email_label = []
            for d in os.listdir(self.train_dir):
                folder = os.path.join(self.train_dir,d)
                self.email_path += [os.path.join(folder,f) for f in os.listdir(folder)]
                self.email_label += [f[0:3]=='spm' for f in os.listdir(folder)]
        # Vectorize emails
        if(verbose): print("email path:", self.email_path)
        self.countvect = CountVectorizer(input='filename',tokenizer=LemmaTokenizer(remove_non_words=True))
        self.word_count = self.countvect.fit_transform(self.email_path)
        self.feat2word = {v: k for k, v in self.countvect.vocabulary_.items()}
        # Tfidf
        self.tfidf_transformer = TfidfTransformer()
        self.tfidf = self.tfidf_transformer.fit_transform(self.word_count)
    def split(self, n, feat='tfidf'):
        if(feat=='tfidf'):
            Xtrain = self.tfidf[:n,:]
            Xtest = self.tfidf[n:,:]
        elif(feat=="wordcount"):
            Xtrain = self.word_count[:n,:]
            Xtest = self.word_count[n:,:]
        ytrain, ytest = np.split(self.email_label,[n])
        return Xtrain, ytrain, Xtest, ytest
    def shuffle_and_split(self, n, feat='tfidf'):
        if(feat=='tfidf'):
            X, y = shuffle(self.tfidf, self.email_label)
        elif(feat=='wordcount'):
            X, y = shuffle(self.word_count, self.email_label)
        Xtrain = X[:n,:]
        Xtest = X[n:,:]
        ytrain, ytest = np.split(y,[n])
        return Xtrain, ytrain, Xtest, ytest
    def print_email(self, email_nb):
        print("email file:", self.email_path[email_nb])
        print("email is a spam:", self.email_label[email_nb])
        print(open(self.email_path[email_nb]).read())
        emailBagOfWords = self.bag_of_words(email_nb)
        print("Bag of words representation (", len(emailBagOfWords), " words in dictionary):", sep='')
        print(emailBagOfWords)
        return
    def email_text(self, email_nb):
        return open(self.email_path[email_nb]).read()
    def email_label(self, email_nb):
        return self.email_label[email_nb]
    def bag_of_words(self, email_nb):
        return {self.feat2word[i]: self.word_count[email_nb, i] for i in self.word_count[email_nb, :].nonzero()[1]}
